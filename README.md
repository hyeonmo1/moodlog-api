
---

```markdown
# MoodLog API  
**AI 기반 감성 분석 & 시각화 일기 서비스 (Backend)**

MoodLog는 사용자가 작성한 일기를 AI가 분석하여  
**요약 · 감정 태그 · 이미지 생성 프롬프트**로 변환하는  
백엔드 중심의 AI 서비스 프로젝트입니다.

본 프로젝트는  
> “LLM을 실제 서비스 아키텍처에 어떻게 안정적으로 통합하는가”  
를 목표로 설계·구현되었습니다.

---

## 👨‍💻 프로젝트 목적 (Why)

이 프로젝트는 단순한 API 연동을 넘어,

- LLM을 **서비스 로직의 한 컴포넌트로 분리**하여 설계
- 외부 API 의존성(OpenAI)에 대한 **에러·쿼터 대응 구조** 구현
- 확장 가능한 REST API 구조 설계

를 통해 **실무형 백엔드 개발 역량**을 증명하는 것을 목표로 합니다.

---

## 🧠 핵심 기능 요약

- 일기 생성 API (POST /api/diaries)
- LLM 기반 감정 분석
  - 요약(summary)
  - 감정 분류(mood)
  - 이미지 생성 프롬프트(image_prompt)
- Mock AI 모드 지원
  - API 크레딧 없이도 전체 플로우 개발 가능
- Swagger 기반 API 문서 자동화

---

##  시스템 설계 개요


Client
↓
FastAPI
├─ API Layer (Request / Response Validation)
├─ Service Layer (LLM / Mock AI)
└─ (확장) Image / DB / Storage


### 설계 포인트
- **Router / Service / Schema 분리**
- HTTP 로직과 AI 로직을 명확히 분리
- 외부 API 장애 시에도 서버 구조 유지 가능

---

##  프로젝트 구조

app/
├─ main.py              # 애플리케이션 진입점
├─ api/
│  └─ routes/
│     └─ diaries.py     # 일기 관련 API
├─ schemas/
│  └─ diary.py          # 요청/응답 데이터 계약
└─ services/
└─ llm.py            # LLM / Mock AI 처리 로직


### 구조 설계 의도
- `schemas`: API 계약 명확화 (Pydantic)
- `services`: 비즈니스 로직 분리 → 테스트/확장 용이
- `routes`: HTTP 관심사만 담당

---

##  LLM 연동 전략 (중요)

### 문제 상황
- OpenAI API는 **쿼터·과금·외부 장애**에 취약
- 개발 중 API 크레딧 부족으로 서비스 중단 가능성 존재

### 해결 전략
 **Mock AI 모드 도입**

```env
MOCK_AI=true
````

* Mock 모드: 키워드 기반 감정 분류 + 더미 프롬프트 반환
* Real 모드: GPT API 호출
* 환경변수 하나로 즉시 전환 가능

### 기대 효과

* 외부 API에 의존하지 않고도 개발 지속
* 테스트 / 로컬 개발 안정성 확보
* 실무에서 자주 사용하는 Stub 패턴 적용

---

## 📡 API 예시

### POST /api/diaries

**Request**

```json
{
  "content": "오늘 팀 프로젝트 발표가 잘 끝나서 뿌듯했다."
}
```

**Response**

```json
{
  "id": 1,
  "content": "오늘 팀 프로젝트 발표가 잘 끝나서 뿌듯했다.",
  "summary": "팀 프로젝트 발표를 성공적으로 마친 하루",
  "mood": "Joy",
  "image_prompt": "A warm watercolor illustration expressing accomplishment and relief"
}
```

---

## ⚙️ 기술 스택

* **Backend**: FastAPI
* **Language**: Python
* **Validation**: Pydantic
* **AI**: OpenAI API (GPT / Mock)
* **Docs**: Swagger (자동 생성)
* **Environment**: dotenv

---

##  확장 계획 (Next Steps)

* 음성 입력(STT, Whisper)
* 이미지 생성(DALL·E / gpt-image-1)
* 이미지 저장(S3)
* 데이터베이스 연동(SQLite → PostgreSQL)
* 감정 히스토리 및 통계 API

---

##  프로젝트를 통해 강조하고 싶은 점

* 단순 API 호출이 아닌 **서비스 구조 관점의 AI 활용**
* 외부 의존성 장애 대응 경험
* REST API 설계 및 데이터 계약(Pydantic) 이해
* 실제 배포 가능한 구조로 확장 가능

---

