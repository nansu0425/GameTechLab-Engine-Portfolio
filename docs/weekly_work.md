# 주차별 작업

- 각 주차에서 **제가 직접 담당한 작업**만 정리한 문서입니다. 팀원이 담당한 영역은 포함하지 않습니다.
- 각 주차의 리포지토리 링크는 **해당 주차 과제까지 진행한 코드베이스의 스냅샷**입니다 
- 원본 팀 작업 리포의 특정 commit을 제 계정에 보존한 것입니다. 

## WEEK01 — 핀볼 게임 (게임잼)

| 기간 | 리포지토리 | 커밋 |
|------|-----------|-----|
| 2025-09-02 ~ 2025-09-04 | [GameTechLab-WEEK01](https://github.com/nansu0425/GameTechLab-WEEK01) | 31건 |

**담당 영역**

| 영역 | 키워드 |
|------|--------|
| **렌더링** | • 사각형/삼각형 프리미티브<br>• 내접원 기반 회전 |
| **물리/충돌** | • Ball-Rectangle/Triangle 충돌<br>• 침투 보정<br>• 속도 반사 |
| **게임플레이** | • 플리퍼(UPadPair) 입력<br>• 탄성/중력 시스템 |

[커밋 기록 보기](commit_history.md#week01-2025-09-02--2025-09-04)

---

## WEEK02 — 3D 씬 에디터 기초

| 기간 | 리포지토리 | 커밋 |
|------|-----------|-----|
| 2025-09-05 ~ 2025-09-11 | [GameTechLab-WEEK02](https://github.com/nansu0425/GameTechLab-WEEK02) | 80건 |

**담당 영역**

| 영역 | 키워드 |
|------|--------|
| **렌더링 파이프라인** | • MVP 변환<br>• 카메라 시스템<br>• RasterizerState |
| **씬 시스템** | • JSON 직렬화<br>• Spawn/Destroy/UUID 관리 |
| **수학/회전** | • 쿼터니언 회전<br>• Euler-Quaternion 변환 |
| **에디터** | • 기즈모 로컬/월드 모드<br>• ImGui UI |

[커밋 기록 보기](commit_history.md#week02-2025-09-05--2025-09-11)

---

## WEEK03 — 엔진 코어 시스템과 에디터 확장

| 기간 | 리포지토리 | 커밋 |
|------|-----------|-----|
| 2025-09-11 ~ 2025-09-18 | [GameTechLab-WEEK03](https://github.com/nansu0425/GameTechLab-WEEK03) | 50건 (nansu0425) |

**담당 영역**

| 영역 | 키워드 |
|------|--------|
| **엔진 코어** | • FName 인터닝<br>• UNamePool<br>• NewObject 팩토리 |
| **메타데이터/RTTI** | • UClass 메타데이터<br>• RTTI 기반 오브젝트 생성 |
| **에디터** | • Scene Manager Panel<br>• View Mode<br>• Show Flag |

[커밋 기록 보기](commit_history.md#week03-2025-09-11--2025-09-17)

---

## WEEK04 — Static Mesh 에셋 파이프라인과 씬 시스템

| 기간 | 리포지토리 | 커밋 |
|------|-----------|-----|
| 2025-09-18 ~ 2025-09-25 | [GameTechLab-WEEK04](https://github.com/nansu0425/GameTechLab-WEEK04) | 52건 (nansu0425 + NanSu) |

**담당 영역**

| 영역 | 키워드 |
|------|--------|
| **에셋 파이프라인** | • UStaticMesh/FStaticMesh<br>• OBJ 로딩/캐싱 |
| **씬 시스템** | • 컴포넌트 단위 직렬화<br>• 카메라 상태 저장/복원 |
| **데이터 무결성** | • UUID 무결성 보장<br>• 레거시 API 마이그레이션 |
| **에디터** | • PropertyWindow<br>• 동적 메시 스폰<br>• Save/Load 패널 |

[커밋 기록 보기](commit_history.md#week04-2025-09-18--2025-09-25)

---

## WEEK05 — 2-Level BVH 피킹 시스템과 Billboard 렌더링

| 기간 | 리포지토리 | 커밋 |
|------|-----------|-----|
| 2025-09-25 ~ 2025-10-02 | [GameTechLab-WEEK05](https://github.com/nansu0425/GameTechLab-WEEK05), [GameTechLab-WEEK05-plus](https://github.com/nansu0425/GameTechLab-WEEK05-plus) | 57건 (nansu0425 — GTLWeek05 40건, Week5_1 17건) |

**담당 영역**

| 영역 | 키워드 |
|------|--------|
| **가속 구조** | • 2-Level BVH (Scene + Mesh)<br>• Binned SAH 분할 |
| **레이 피킹** | • 프론트-투-백 트래버설<br>• Back-face Culling<br>• O(N)→O(log N) |
| **성능 최적화** | • Dirty Flag Refit<br>• SoA 캐시<br>• 프로파일링 |
| **렌더링** | • Billboard/TextRender 이원 구조 재설계 |

[커밋 기록 보기](commit_history.md#week05-2025-09-26--2025-10-02)

---

## WEEK06 — 데칼 시스템, Scene Depth, Exponential Height Fog

| 기간 | 리포지토리 | 커밋 |
|------|-----------|-----|
| 2025-10-10 ~ 2025-10-15 | [GameTechLab-WEEK06](https://github.com/nansu0425/GameTechLab-WEEK06), [GameTechLab-WEEK06-plus](https://github.com/nansu0425/GameTechLab-WEEK06-plus) | 37건 (nansu0425 + NanSu) |

**담당 영역**

| 영역 | 키워드 |
|------|--------|
| **데칼 시스템** | • Show Flag<br>• OBB 시각화<br>• 통계 오버레이 |
| **포스트 프로세싱** | • Scene Depth 시각화<br>• Exponential Height Fog |
| **렌더링 인프라** | • Render Target 분리<br>• Resource Hazard 해결 |

[커밋 기록 보기](commit_history.md#week06-2025-10-10--2025-10-15)

---

## WEEK07 — UberLit 조명 시스템과 셰이더 인프라 고도화

| 기간 | 리포지토리 | 커밋 |
|------|-----------|-----|
| 2025-10-16 ~ 2025-10-22 | [GameTechLab-WEEK07](https://github.com/nansu0425/GameTechLab-WEEK07) | 127건 (nansu0425 + NanSu) |

**담당 영역**

| 영역 | 키워드 |
|------|--------|
| **조명 시스템** | • 4종 라이트<br>• Blinn-Phong<br>• 색온도<br>• 감쇠 모델 |
| **셰이더 인프라** | • 셰이더 핫 리로드<br>• DDS 텍스처 베이킹 |
| **렌더링 확장** | • World Normal 뷰 모드<br>• 데칼 라이팅<br>• 디버그 볼륨 |

[커밋 기록 보기](commit_history.md#week07-2025-10-16--2025-10-22)

---

## WEEK08 — Shadow Mapping 시스템 (Directional / Spot / Point, PCF, PSM)

| 기간 | 리포지토리 | 커밋 |
|------|-----------|-----|
| 2025-10-24 ~ 2025-10-29 | [GameTechLab-WEEK08](https://github.com/nansu0425/GameTechLab-WEEK08) | 27건 (nansu0425 + NanSu) |

**담당 영역**

| 영역 | 키워드 |
|------|--------|
| **그림자 시스템** | • Directional/Spot/Point Shadow Mapping<br>• Cube SM |
| **그림자 품질** | • PCF 소프트 섀도우<br>• PSM<br>• LiSPSM |
| **렌더링 인프라** | • Shadow Map 리소스 관리<br>• DepthOnly 패스 |

[커밋 기록 보기](commit_history.md#week08-2025-10-24--2025-10-29)

---

## WEEK09 — 탑다운 슈팅 게임 (게임잼)

| 기간 | 리포지토리 | 커밋 |
|------|-----------|-----|
| 2025-10-30 ~ 2025-11-06 | [GameTechLab-WEEK09](https://github.com/nansu0425/GameTechLab-WEEK09), [GameTechLab-WEEK09-plus](https://github.com/nansu0425/GameTechLab-WEEK09-plus) | 94건 비병합 (nansu0425 + NanSu) |

**담당 영역**

| 영역 | 키워드 |
|------|--------|
| **스크립팅** | • Lua(Sol2) 통합<br>• 메타테이블 프록시<br>• 핫 리로딩 |
| **충돌/이벤트** | • Shape 컴포넌트(Box/Sphere/Capsule)<br>• Overlap 이벤트 |
| **게임플레이** | • 3종 투사체<br>• PIE 모드 객체 복제/정리 |
| **연출** | • PlayerCameraManager<br>• 카메라 쉐이크/트랜지션 |

[커밋 기록 보기](commit_history.md#week09-2025-10-30--2025-11-06)

---

## WEEK10 — FBX Import 파이프라인과 Skeletal Mesh 시스템

| 기간 | 리포지토리 | 커밋 |
|------|-----------|-----|
| 2025-11-07 ~ 2025-11-12 | [GameTechLab-WEEK10](https://github.com/nansu0425/GameTechLab-WEEK10) | 54건 (nansu0425 + NanSu) |

**담당 영역**

| 영역 | 키워드 |
|------|--------|
| **FBX 통합** | • FBX SDK<br>• Static/Skeletal 자동 감지<br>• 좌표계 변환 |
| **스켈레탈 메시** | • Skeleton 추출<br>• Skin Weights 병합<br>• CPU Skinning |
| **성능** | • FBX 바이너리 캐싱<br>• Vertex Welding |
| **에디터** | • FBX Import 툴바<br>• Console Panel<br>• Show Flag |

[커밋 기록 보기](commit_history.md#week10-2025-11-07--2025-11-12)

---

## WEEK11 — FBX 애니메이션 Import와 Skeleton 교체 시스템

| 기간 | 리포지토리 | 커밋 |
|------|-----------|-----|
| 2025-11-13 ~ 2025-11-19 | [GameTechLab-WEEK11](https://github.com/nansu0425/GameTechLab-WEEK11) | 45건 비병합 (nansu0425 + NanSu) |

**담당 영역**

| 영역 | 키워드 |
|------|--------|
| **애니메이션 Import** | • AnimStack 키프레임 추출<br>• 애니메이션 캐싱 |
| **호환성** | • Mixamo/Blender FBX 처리<br>• Winding Order 자동 감지 |
| **아키텍처** | • UE5 패턴 리팩토링<br>• Plugins/Fbx 모듈 분리 |
| **에디터** | • Skeleton 교체 UI<br>• AnimToPlay 드롭다운 |

[커밋 기록 보기](commit_history.md#week11-2025-11-13--2025-11-19)

---

## WEEK12 — Particle System 에셋 설계와 충돌/이벤트 시스템

| 기간 | 리포지토리 | 커밋 |
|------|-----------|-----|
| 2025-11-21 ~ 2025-11-26 | [GameTechLab-WEEK12](https://github.com/nansu0425/GameTechLab-WEEK12) | 45건 (nansu0425) |

**담당 영역**

| 영역 | 키워드 |
|------|--------|
| **에셋 설계** | • 4단계 계층(System→Emitter→LOD→Module)<br>• FBaseParticle |
| **파티클 모듈** | • 10종 기본 모듈<br>• 충돌(Bounce/Kill/Stop)<br>• EventGenerator |
| **엔진 인프라** | • enum UPROPERTY 리플렉션<br>• 직렬화/Template 관리 |
| **디버깅** | • Symbol Server<br>• Source Link |

[커밋 기록 보기](commit_history.md#week12-2025-11-21--2025-11-26)

---

## WEEK13 — PhysX 물리 시스템 통합과 Ragdoll, DoF, Camera Pilot

| 기간 | 리포지토리 | 커밋 |
|------|-----------|-----|
| 2025-11-28 ~ 2025-12-04 | [GameTechLab-WEEK13](https://github.com/nansu0425/GameTechLab-WEEK13) | 105건 (nansu0425) |

**담당 영역**

| 영역 | 키워드 |
|------|--------|
| **물리 코어** | • PhysX 4.1 통합<br>• PhysicsCore/PhysScene<br>• PIMPL |
| **물리 브릿지** | • FBodyInstance/UBodySetup<br>• Fixed Timestep<br>• 렌더 보간 |
| **래그돌** | • SkeletalMesh Ragdoll<br>• 자동 Constraint 생성 |
| **에디터/후처리** | • Camera Pilot<br>• Depth of Field(Multi-pass) |

[커밋 기록 보기](commit_history.md#week13-2025-11-28--2025-12-04)

---

## WEEK14 — FPS 좀비 서바이벌 게임 (게임잼)

| 기간 | 리포지토리 | 커밋 |
|------|-----------|-----|
| 2025-12-05 ~ 2025-12-11 | [GameTechLab-WEEK14](https://github.com/nansu0425/GameTechLab-WEEK14) | 37건 (nansu0425) |

**담당 영역**

| 영역 | 키워드 |
|------|--------|
| **포스트 프로세스** | • 피격 이펙트 3종(Fire/Slime/Electric)<br>• HLSL 셰이더 |
| **게임플레이** | • Red Dot Sight<br>• ADS 전환<br>• DoF 블러 연동 |
| **렌더링** | • UberLit Alpha Test/Discard<br>• 식생 렌더링 |
| **에셋 제작** | • GrassTile<br>• 나무<br>• 울타리<br>• Hulk Zombie |

[커밋 기록 보기](commit_history.md#week14-2025-12-05--2025-12-11)
