# 주차별 작업

## WEEK01 — 핀볼 게임 (게임잼)

| 기간 | 리포지토리 | 커밋 |
|------|-----------|-----|
| 2025-09-02 ~ 2025-09-04 | [pinball-game](https://github.com/TraceofLight/pinball-game) | 31건 |

첫 주차 게임잼으로 DX11 기반 2D 핀볼 게임을 제작했다.
기존 렌더러 위에 URectangle/UTriangle 렌더링, 충돌 처리, 플리퍼(UPadPair) 입력 시스템을 구현했다.

**담당 영역**

| 영역 | 키워드 |
|------|--------|
| **렌더링** | 사각형/삼각형 프리미티브, 내접원 기반 회전 |
| **물리/충돌** | Ball-Rectangle/Triangle 충돌, 침투 보정, 속도 반사 |
| **게임플레이** | 플리퍼(UPadPair) 입력, 탄성/중력 시스템 |

[커밋 기록 보기](commit_history.md#week01-2025-09-02--2025-09-04)

---

## WEEK02 — 3D 씬 에디터 기초

| 기간 | 리포지토리 | 커밋 |
|------|-----------|-----|
| 2025-09-05 ~ 2025-09-11 | [GTL-Week02](https://github.com/Jeongwoohyeong/GTL-Week02) | 80건 |

DX11 렌더링 파이프라인 위에 3D 씬 에디터의 핵심 기능을 구현했다.
RasterizerState, MVP 변환, 씬 직렬화, 쿼터니언 회전 시스템, 기즈모, ImGui 에디터 UI까지 에디터의 기반을 완성했다.

**담당 영역**

| 영역 | 키워드 |
|------|--------|
| **렌더링 파이프라인** | MVP 변환, 카메라 시스템, RasterizerState |
| **씬 시스템** | JSON 직렬화, Spawn/Destroy/UUID 관리 |
| **수학/회전** | 쿼터니언 회전, Euler-Quaternion 변환 |
| **에디터** | 기즈모 로컬/월드 모드, ImGui UI |

[커밋 기록 보기](commit_history.md#week02-2025-09-05--2025-09-11)

---

## WEEK03 — 엔진 코어 시스템과 에디터 확장

| 기간 | 리포지토리 | 커밋 |
|------|-----------|-----|
| 2025-09-11 ~ 2025-09-18 | [Krafton_TechLab_Week03](https://github.com/TeshShin/Krafton_TechLab_Week03) | 50건 (nansu0425) |

엔진의 핵심 인프라를 구축했다.
FName/UNamePool 문자열 인터닝, RTTI 기반 NewObject 팩토리, UClass 메타데이터 시스템을 구현하고,
Scene Manager Panel, View Mode, Show Flag 등 에디터 기능을 확장했다.

**담당 영역**

| 영역 | 키워드 |
|------|--------|
| **엔진 코어** | FName 인터닝, UNamePool, NewObject 팩토리 |
| **메타데이터/RTTI** | UClass 메타데이터, RTTI 기반 오브젝트 생성 |
| **에디터** | Scene Manager Panel, View Mode, Show Flag |

[커밋 기록 보기](commit_history.md#week03-2025-09-11--2025-09-17)

---

## WEEK04 — Static Mesh 에셋 파이프라인과 씬 시스템

| 기간 | 리포지토리 | 커밋 |
|------|-----------|-----|
| 2025-09-18 ~ 2025-09-25 | [KRAFTON_TechLab_Engine](https://github.com/JeongBeomLee/KRAFTON_TechLab_Engine) | 52건 (nansu0425 + NanSu) |

에셋 파이프라인과 씬 시스템을 전면 재설계했다.
UStaticMesh/FStaticMesh 파이프라인 구축, OBJ 모델 로딩/캐싱(FObjManager),
컴포넌트 단위 직렬화, 카메라 상태 저장/복원, UUID 무결성 보장, PropertyWindow UI를 구현했다.

**담당 영역**

| 영역 | 키워드 |
|------|--------|
| **에셋 파이프라인** | UStaticMesh/FStaticMesh, OBJ 로딩/캐싱 |
| **씬 시스템** | 컴포넌트 단위 직렬화, 카메라 상태 저장/복원 |
| **데이터 무결성** | UUID 무결성 보장, 레거시 API 마이그레이션 |
| **에디터** | PropertyWindow, 동적 메시 스폰, Save/Load 패널 |

[커밋 기록 보기](commit_history.md#week04-2025-09-18--2025-09-25)

---

## WEEK05 — 2-Level BVH 피킹 시스템과 Billboard 렌더링

| 기간 | 리포지토리 | 커밋 |
|------|-----------|-----|
| 2025-09-25 ~ 2025-10-02 | [GTLWeek05](https://github.com/Sunha-i/GTLWeek05), [Week5_1](https://github.com/nayechan/Week5_1) | 57건 (nansu0425 — GTLWeek05 40건, Week5_1 17건) |

씬 레벨·메시 레벨 2-Level BVH를 구축하여 레이 피킹을 O(N)에서 O(log N)으로 가속했다.
Binned SAH 분할, Dirty Flag Refit, 프론트-투-백 조기 가지치기, Back-face Culling 등 최적화를 적용하고,
UTextRenderComponent + UBillboardComponent 이원 구조를 재설계했다.

**담당 영역**

| 영역 | 키워드 |
|------|--------|
| **가속 구조** | 2-Level BVH (Scene + Mesh), Binned SAH 분할 |
| **레이 피킹** | 프론트-투-백 트래버설, Back-face Culling, O(N)→O(log N) |
| **성능 최적화** | Dirty Flag Refit, SoA 캐시, 프로파일링 |
| **렌더링** | Billboard/TextRender 이원 구조 재설계 |

[커밋 기록 보기](commit_history.md#week05-2025-09-26--2025-10-02)

---

## WEEK06 — 데칼 시스템, Scene Depth, Exponential Height Fog

| 기간 | 리포지토리 | 커밋 |
|------|-----------|-----|
| 2025-10-10 ~ 2025-10-15 | [KRAFTON_JungleTechLab_Week06](https://github.com/Kim-yunsoo/KRAFTON_JungleTechLab_Week06) | 37건 (nansu0425 + NanSu) |

렌더링 파이프라인을 대폭 확장했다.
데칼 Show Flag/OBB 시각화/통계 오버레이, Scene Depth 시각화 뷰 모드,
Exponential Height Fog 포스트 프로세싱을 구현하고, Scene Render Target 분리와 Resource Hazard 해결 등 인프라를 정비했다.

**담당 영역**

| 영역 | 키워드 |
|------|--------|
| **데칼 시스템** | Show Flag, OBB 시각화, 통계 오버레이 |
| **포스트 프로세싱** | Scene Depth 시각화, Exponential Height Fog |
| **렌더링 인프라** | Render Target 분리, Resource Hazard 해결 |

[커밋 기록 보기](commit_history.md#week06-2025-10-10--2025-10-15)

---

## WEEK07 — UberLit 조명 시스템과 셰이더 인프라 고도화

| 기간 | 리포지토리 | 커밋 |
|------|-----------|-----|
| 2025-10-16 ~ 2025-10-22 | [Krafton_TechLab_Week14](https://github.com/Budnarae/Krafton_TechLab_Week14) | 127건 (nansu0425 + NanSu) |

UberLit 셰이더를 중심으로 Ambient/Directional/Point/Spot 4종 라이트를 구현했다.
Inverse Square / Exponent Falloff 감쇠, 색온도, Blinn-Phong/Phong 전환 등 물리 기반 조명을 완성하고,
셰이더 핫 리로드(include 의존성 추적), DDS 텍스처 베이킹(DirectXTex), 한글 경로 호환, World Normal 시각화 뷰 모드, 라이트 디버그 볼륨을 구현했다.

**담당 영역**

| 영역 | 키워드 |
|------|--------|
| **조명 시스템** | 4종 라이트, Blinn-Phong, 색온도, 감쇠 모델 |
| **셰이더 인프라** | 셰이더 핫 리로드, DDS 텍스처 베이킹 |
| **렌더링 확장** | World Normal 뷰 모드, 데칼 라이팅, 디버그 볼륨 |

[커밋 기록 보기](commit_history.md#week07-2025-10-16--2025-10-22)

---

## WEEK08 — Shadow Mapping 시스템 (Directional / Spot / Point, PCF, PSM)

| 기간 | 리포지토리 | 커밋 |
|------|-----------|-----|
| 2025-10-24 ~ 2025-10-29 | [FutureEngine](https://github.com/nansu0425/FutureEngine) | 27건 (nansu0425 + NanSu) |

Directional/Spot/Point 3종 라이트에 Shadow Mapping을 구현했다.
PCF(Percentage Closer Filtering)로 소프트 섀도우를 적용하고,
Perspective Shadow Mapping(PSM)과 LiSPSM 투영 모드로 그림자 품질을 개선했다.

**담당 영역**

| 영역 | 키워드 |
|------|--------|
| **그림자 시스템** | Directional/Spot/Point Shadow Mapping, Cube SM |
| **그림자 품질** | PCF 소프트 섀도우, PSM, LiSPSM |
| **렌더링 인프라** | Shadow Map 리소스 관리, DepthOnly 패스 |

[커밋 기록 보기](commit_history.md#week08-2025-10-24--2025-10-29)

---

## WEEK09 — 탑다운 슈팅 게임 (게임잼)

| 기간 | 리포지토리 | 커밋 |
|------|-----------|-----|
| 2025-10-30 ~ 2025-11-06 | [FutureEngine](https://github.com/nansu0425/FutureEngine) | 94건 비병합 (nansu0425 + NanSu) |

자체 엔진으로 탑다운 슈팅 게임을 제작하는 게임잼.
Lua(Sol2) 스크립팅 시스템, Shape 컴포넌트 충돌/Overlap 이벤트,
직선/유도/궤도 3종 투사체, PlayerCameraManager, 카메라 쉐이크/트랜지션, PIE 안전 처리를 구현했다.

**담당 영역**

| 영역 | 키워드 |
|------|--------|
| **스크립팅** | Lua(Sol2) 통합, 메타테이블 프록시, 핫 리로딩 |
| **충돌/이벤트** | Shape 컴포넌트(Box/Sphere/Capsule), Overlap 이벤트 |
| **게임플레이** | 3종 투사체, PIE 모드 객체 복제/정리 |
| **연출** | PlayerCameraManager, 카메라 쉐이크/트랜지션 |

[커밋 기록 보기](commit_history.md#week09-2025-10-30--2025-11-06)

---

## WEEK10 — FBX Import 파이프라인과 Skeletal Mesh 시스템

| 기간 | 리포지토리 | 커밋 |
|------|-----------|-----|
| 2025-11-07 ~ 2025-11-12 | [Mundi_Week10](https://github.com/fuenell/Mundi_Week10) | 54건 (nansu0425 + NanSu) |

FBX SDK를 통합하고 Skeletal Mesh 시스템을 전면 구축했다.
Static/Skeletal Mesh 자동 감지, 좌표계 변환(RH→LH), Skeleton 추출, Skin Weights 병합,
CPU Skinning, Vertex Welding, FBX 바이너리 캐싱, Console Panel 개선을 구현했다.

**담당 영역**

| 영역 | 키워드 |
|------|--------|
| **FBX 통합** | FBX SDK, Static/Skeletal 자동 감지, 좌표계 변환 |
| **스켈레탈 메시** | Skeleton 추출, Skin Weights 병합, CPU Skinning |
| **성능** | FBX 바이너리 캐싱, Vertex Welding |
| **에디터** | FBX Import 툴바, Console Panel, Show Flag |

[커밋 기록 보기](commit_history.md#week10-2025-11-07--2025-11-12)

---

## WEEK11 — FBX 애니메이션 Import와 Skeleton 교체 시스템

| 기간 | 리포지토리 | 커밋 |
|------|-----------|-----|
| 2025-11-13 ~ 2025-11-19 | [Krafton_TechLab_Week14](https://github.com/Budnarae/Krafton_TechLab_Week14), [Week11_4](https://github.com/nayechan/Week11_4) | 45건 비병합 (nansu0425 + NanSu) |

FBX AnimStack에서 Bone별 키프레임을 추출하는 애니메이션 Import를 완성했다.
Mixamo/Blender FBX 호환, Winding Order 자동 감지, UE5 아키텍처 리팩토링(Plugins/Fbx),
AnimToPlay 드롭다운 필터링, 런타임 Skeleton 교체 UI와 .skeleton 오버라이드 직렬화를 구현했다.

**담당 영역**

| 영역 | 키워드 |
|------|--------|
| **애니메이션 Import** | AnimStack 키프레임 추출, 애니메이션 캐싱 |
| **호환성** | Mixamo/Blender FBX 처리, Winding Order 자동 감지 |
| **아키텍처** | UE5 패턴 리팩토링, Plugins/Fbx 모듈 분리 |
| **에디터** | Skeleton 교체 UI, AnimToPlay 드롭다운 |

[커밋 기록 보기](commit_history.md#week11-2025-11-13--2025-11-19)

---

## WEEK12 — Particle System 에셋 설계와 충돌/이벤트 시스템

| 기간 | 리포지토리 | 커밋 |
|------|-----------|-----|
| 2025-11-21 ~ 2025-11-26 | [KraftonGTL_week12](https://github.com/lorevoon/KraftonGTL_week12) | 45건 (nansu0425) |

UE5 Cascade 구조를 참조하여 Particle System 에셋 계층(4단계)을 설계했다.
FBaseParticle(128B) 데이터 레이아웃과 10종 기본 모듈, 파티클 충돌(Line Trace + Bounce/Kill/Stop),
EventGenerator 이벤트 델리게이트, enum UPROPERTY 리플렉션, Symbol Server/Source Link 디버깅 인프라를 구현했다.

**담당 영역**

| 영역 | 키워드 |
|------|--------|
| **에셋 설계** | 4단계 계층(System→Emitter→LOD→Module), FBaseParticle |
| **파티클 모듈** | 10종 기본 모듈, 충돌(Bounce/Kill/Stop), EventGenerator |
| **엔진 인프라** | enum UPROPERTY 리플렉션, 직렬화/Template 관리 |
| **디버깅** | Symbol Server, Source Link |

[커밋 기록 보기](commit_history.md#week12-2025-11-21--2025-11-26)

---

## WEEK13 — PhysX 물리 시스템 통합과 Ragdoll, DoF, Camera Pilot

| 기간 | 리포지토리 | 커밋 |
|------|-----------|-----|
| 2025-11-28 ~ 2025-12-04 | [Krafton_TechLab_Week13](https://github.com/Sunha-i/Krafton_TechLab_Week13) | 105건 (nansu0425) |

PhysX 4.1을 통합하여 물리 시뮬레이션 인프라를 구축했다.
PhysicsCore/PhysScene 분리, FBodyInstance/UBodySetup 브릿지, Fixed Timestep + 렌더 보간,
비동기 시뮬레이션, Ragdoll(자동 Constraint 생성), Physics Asset Editor,
Camera Pilot 모드, Depth of Field Multi-pass(6셰이더)를 구현했다.

**담당 영역**

| 영역 | 키워드 |
|------|--------|
| **물리 코어** | PhysX 4.1 통합, PhysicsCore/PhysScene, PIMPL |
| **물리 브릿지** | FBodyInstance/UBodySetup, Fixed Timestep, 렌더 보간 |
| **래그돌** | SkeletalMesh Ragdoll, 자동 Constraint 생성 |
| **에디터/후처리** | Camera Pilot, Depth of Field(Multi-pass) |

[커밋 기록 보기](commit_history.md#week13-2025-11-28--2025-12-04)

---

## WEEK14 — FPS 좀비 서바이벌 게임 (게임잼)

| 기간 | 리포지토리 | 커밋 |
|------|-----------|-----|
| 2025-12-05 ~ 2025-12-11 | [Krafton_TechLab_Week14](https://github.com/Budnarae/Krafton_TechLab_Week14) | 37건 (nansu0425) |

자체 엔진으로 FPS 좀비 서바이벌 게임을 제작하는 게임잼.
Fire/Slime/Electric 3종 포스트 프로세스 피격 이펙트를 HLSL + 카메라 모디파이어로 구현하고,
Red Dot Sight ADS 전환 시 DoF 블러 적용, UberLit Alpha Test/Discard 식생 렌더링,
GrassTile/나무/울타리/Hulk Zombie skeletal mesh 등 다수의 3D 에셋을 제작했다.

**담당 영역**

| 영역 | 키워드 |
|------|--------|
| **포스트 프로세스** | 피격 이펙트 3종(Fire/Slime/Electric), HLSL 셰이더 |
| **게임플레이** | Red Dot Sight, ADS 전환, DoF 블러 연동 |
| **렌더링** | UberLit Alpha Test/Discard, 식생 렌더링 |
| **에셋 제작** | GrassTile, 나무, 울타리, Hulk Zombie |

[커밋 기록 보기](commit_history.md#week14-2025-12-05--2025-12-11)
