"""build_commit_history.py — Generate docs/commit_history.md from snapshot repos.

For each node in NODES (a time-ordered chain of personal snapshot repos
nansu0425/GameTechLab-WEEKxx[-plus]), select MY commits whose timestamp falls
in the half-open window (previous-node-boundary, this-node-boundary] where
boundary(N) is the latest MY commit's timestamp in repo N. Render as a
### WEEKxx[+] section in the output document.

This produces a commit history that is, by construction, an exact partition of
my commits across the snapshot repos linked from docs/weekly_work.md.

Usage
-----
    python scripts/build_commit_history.py                  # write docs/commit_history.md
    python scripts/build_commit_history.py --dry-run        # print to stdout
    python scripts/build_commit_history.py --output X.md    # write to X.md
    python scripts/build_commit_history.py --cache-dir .cache/commits  # read/write JSON cache

Environment
-----------
    GITHUB_TOKEN    Personal access token (optional but recommended; lifts the
                    GitHub API rate limit from 60 to 5000 req/hr).

Notes
-----
- Standard library only, no `pip install` required.
- "MY commits" = author.login in MY_LOGINS or commit.author.name in MY_NAMES.
  If the script encounters a likely-mine identifier not in those sets, add it.
- WEEK05/06/09 each appear twice in NODES — once for the main 정과제 snapshot
  and once for the +과제 snapshot — and become two peer ### sections.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone, timedelta
from pathlib import Path

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

NODES = [
    {"id": "WEEK01",  "repo": "nansu0425/GameTechLab-WEEK01"},
    {"id": "WEEK02",  "repo": "nansu0425/GameTechLab-WEEK02"},
    {"id": "WEEK03",  "repo": "nansu0425/GameTechLab-WEEK03"},
    {"id": "WEEK04",  "repo": "nansu0425/GameTechLab-WEEK04"},
    {"id": "WEEK05",  "repo": "nansu0425/GameTechLab-WEEK05"},
    {"id": "WEEK05+", "repo": "nansu0425/GameTechLab-WEEK05-plus"},
    {"id": "WEEK06",  "repo": "nansu0425/GameTechLab-WEEK06"},
    {"id": "WEEK06+", "repo": "nansu0425/GameTechLab-WEEK06-plus"},
    {"id": "WEEK07",  "repo": "nansu0425/GameTechLab-WEEK07"},
    {"id": "WEEK08",  "repo": "nansu0425/GameTechLab-WEEK08"},
    {"id": "WEEK09",  "repo": "nansu0425/GameTechLab-WEEK09"},
    {"id": "WEEK09+", "repo": "nansu0425/GameTechLab-WEEK09-plus"},
    {"id": "WEEK10",  "repo": "nansu0425/GameTechLab-WEEK10"},
    {"id": "WEEK11",  "repo": "nansu0425/GameTechLab-WEEK11"},
    {"id": "WEEK12",  "repo": "nansu0425/GameTechLab-WEEK12"},
    {"id": "WEEK13",  "repo": "nansu0425/GameTechLab-WEEK13"},
    {"id": "WEEK14",  "repo": "nansu0425/GameTechLab-WEEK14"},
]

MY_LOGINS = {"nansu0425"}
MY_NAMES = {"NanSu", "nansu0425"}

GITHUB_API = "https://api.github.com"
USER_AGENT = "build_commit_history (nansu0425)"
KST = timezone(timedelta(hours=9))

DEFAULT_OUTPUT = Path("docs/commit_history.md")


# ---------------------------------------------------------------------------
# GitHub API
# ---------------------------------------------------------------------------

def _request(url: str):
    req = urllib.request.Request(url, headers={
        "User-Agent": USER_AGENT,
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    })
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    try:
        with urllib.request.urlopen(req) as resp:
            return json.load(resp)
    except urllib.error.HTTPError as e:
        if e.code in (403, 429):
            reset = int(e.headers.get("X-RateLimit-Reset", "0") or 0)
            if reset:
                wait = max(0, reset - int(time.time())) + 5
                print(f"Rate-limited. Sleeping {wait}s until reset.", file=sys.stderr)
                time.sleep(wait)
                return _request(url)
            print(
                "Rate-limited and no reset header. Set GITHUB_TOKEN to raise the limit.",
                file=sys.stderr,
            )
        raise


def fetch_commits(repo: str, cache_dir: Path | None = None) -> list[dict]:
    """Return all commits on the repo's default branch with the fields we need.

    If cache_dir is given, read from / write to <cache_dir>/<owner>__<name>.json
    so reruns don't burn API quota.
    """
    cache_path: Path | None = None
    if cache_dir is not None:
        cache_path = cache_dir / (repo.replace("/", "__") + ".json")
        if cache_path.exists():
            return json.loads(cache_path.read_text(encoding="utf-8"))

    out: list[dict] = []
    page = 1
    while True:
        url = f"{GITHUB_API}/repos/{repo}/commits?per_page=100&page={page}"
        data = _request(url)
        if not data:
            break
        for c in data:
            author_obj = c.get("author") or {}
            commit = c.get("commit") or {}
            cauth = commit.get("author") or {}
            message = commit.get("message") or ""
            out.append({
                "sha": c["sha"],
                "login": author_obj.get("login"),
                "name": cauth.get("name"),
                "date": cauth.get("date"),
                "message": message.splitlines()[0] if message else "",
            })
        if len(data) < 100:
            break
        page += 1

    if cache_path is not None:
        cache_path.parent.mkdir(parents=True, exist_ok=True)
        cache_path.write_text(json.dumps(out, ensure_ascii=False), encoding="utf-8")

    return out


# ---------------------------------------------------------------------------
# Filtering and boundary logic
# ---------------------------------------------------------------------------

def is_mine(c: dict) -> bool:
    return (c.get("login") in MY_LOGINS) or (c.get("name") in MY_NAMES)


def parse_iso(s: str) -> datetime:
    return datetime.fromisoformat(s.replace("Z", "+00:00"))


def fmt_kst_date(iso: str) -> str:
    return parse_iso(iso).astimezone(KST).strftime("%Y-%m-%d")


def short_sha(sha: str) -> str:
    return sha[:7]


def slugify(heading: str) -> str:
    """Approximate GitHub auto-anchor: lowercase, spaces→'-', drop punctuation
    other than '-'/'_', preserve alphanumerics (Hangul included)."""
    out: list[str] = []
    for ch in heading.lower():
        if ch.isalnum() or ch in ("-", "_"):
            out.append(ch)
        elif ch == " ":
            out.append("-")
    return "".join(out)


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------

def render_section_table(commits: list[dict], repo: str) -> str:
    lines = [
        "| 날짜 | SHA | 커밋 메시지 |",
        "|------|-----|------------|",
    ]
    for c in commits:
        date = fmt_kst_date(c["date"])
        sha7 = short_sha(c["sha"])
        url = f"https://github.com/{repo}/commit/{c['sha']}"
        msg = c["message"].replace("|", "\\|")
        lines.append(f"| {date} | [{sha7}]({url}) | {msg} |")
    return "\n".join(lines)


def render_document(node_data: list[tuple[dict, list[dict]]]) -> str:
    populated = [(n, cs) for n, cs in node_data if cs]
    total_commits = sum(len(cs) for _, cs in populated)
    repo_count = len(populated)

    all_commits = [c for _, cs in populated for c in cs]
    first_date = fmt_kst_date(min(c["date"] for c in all_commits))
    last_date = fmt_kst_date(max(c["date"] for c in all_commits))

    weeks_seen: set[str] = set()
    for n, _ in populated:
        weeks_seen.add(n["id"].rstrip("+"))
    week_count = len(weeks_seen)

    lines: list[str] = []

    # ── Header ──────────────────────────────────────────────────────────
    lines.append("# 커밋 기록")
    lines.append("")
    lines.append(f"**기간:** {first_date} ~ {last_date}  ")
    lines.append("**GitHub:** [nansu0425](https://github.com/nansu0425)  ")
    lines.append(f"**고유 커밋 수:** {total_commits}건  ")
    lines.append(f"**참여 주차:** {week_count}개 주차  ")
    lines.append(f"**기여 Repository:** {repo_count}개")
    lines.append("")
    lines.append("---")
    lines.append("")

    def date_range_for(commits: list[dict]) -> str:
        return f"{fmt_kst_date(commits[0]['date'])} ~ {fmt_kst_date(commits[-1]['date'])}"

    # ── ToC ─────────────────────────────────────────────────────────────
    lines.append("## 목차")
    lines.append("")
    lines.append("- [주차별 참여 요약](#주차별-참여-요약)")
    lines.append("- [주차별 커밋 기록](#주차별-커밋-기록)")
    for n, cs in populated:
        heading = f"{n['id']} ({date_range_for(cs)})"
        lines.append(f"  - [{heading}](#{slugify(heading)})")
    lines.append("")
    lines.append("---")
    lines.append("")

    # ── Weekly summary (with repo link) ─────────────────────────────────
    lines.append("## 주차별 참여 요약")
    lines.append("")
    lines.append("| 주차 | 기간 | 리포지토리 | 고유 커밋 수 |")
    lines.append("|------|------|-----------|------------|")
    for n, cs in populated:
        repo = n["repo"]
        repo_short = repo.split("/", 1)[1]
        repo_link = f"[{repo_short}](https://github.com/{repo})"
        lines.append(f"| {n['id']} | {date_range_for(cs)} | {repo_link} | {len(cs)}건 |")
    lines.append("")
    lines.append("---")
    lines.append("")

    # ── Weekly records ──────────────────────────────────────────────────
    lines.append("## 주차별 커밋 기록")
    lines.append("")
    for n, cs in populated:
        lines.append(f"### {n['id']} ({date_range_for(cs)})")
        lines.append("")
        lines.append(render_section_table(cs, n["repo"]))
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate docs/commit_history.md from personal snapshot repos.",
    )
    parser.add_argument("--dry-run", action="store_true", help="Print to stdout instead of writing a file.")
    parser.add_argument(
        "--output", type=Path, default=DEFAULT_OUTPUT,
        help=f"Output path (default: {DEFAULT_OUTPUT}).",
    )
    parser.add_argument(
        "--cache-dir", type=Path, default=None,
        help="Cache GitHub API responses as JSON files in this dir to avoid refetching.",
    )
    args = parser.parse_args()

    if not os.environ.get("GITHUB_TOKEN"):
        print(
            "Note: GITHUB_TOKEN not set; rate limit is 60 req/hr. "
            "Set it (e.g., a no-scope PAT) to lift to 5000.",
            file=sys.stderr,
        )

    # Fetch
    print("Fetching commits...", file=sys.stderr)
    repo_commits: dict[str, list[dict]] = {}
    for node in NODES:
        print(f"  {node['repo']}", file=sys.stderr, flush=True)
        repo_commits[node["id"]] = fetch_commits(node["repo"], args.cache_dir)
    total_fetched = sum(len(v) for v in repo_commits.values())
    print(f"Fetched {total_fetched} commits across {len(NODES)} nodes.", file=sys.stderr)

    # Boundary chain + filtering
    node_data: list[tuple[dict, list[dict]]] = []
    prev_boundary = datetime.fromtimestamp(0, tz=timezone.utc)
    for node in NODES:
        commits = repo_commits[node["id"]]
        my_commits = [c for c in commits if is_mine(c) and c.get("date")]
        if not my_commits:
            print(f"WARN: no my-commits in {node['id']} ({node['repo']})", file=sys.stderr)
            node_data.append((node, []))
            continue
        boundary = max(parse_iso(c["date"]) for c in my_commits)
        if boundary <= prev_boundary:
            print(
                f"WARN: boundary regression at {node['id']}: boundary={boundary.isoformat()} "
                f"<= prev={prev_boundary.isoformat()}",
                file=sys.stderr,
            )
        in_window = [
            c for c in my_commits
            if prev_boundary < parse_iso(c["date"]) <= boundary
        ]
        in_window.sort(key=lambda c: parse_iso(c["date"]))
        node_data.append((node, in_window))
        prev_boundary = boundary
        print(
            f"  {node['id']}: {len(in_window)} my-commits in window "
            f"(boundary={boundary.astimezone(KST).strftime('%Y-%m-%d %H:%M %Z')})",
            file=sys.stderr,
        )

    # Render and emit
    doc = render_document(node_data)
    if args.dry_run:
        sys.stdout.write(doc)
        return 0
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(doc, encoding="utf-8", newline="\n")
    print(f"Wrote {args.output} ({len(doc):,} chars)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
