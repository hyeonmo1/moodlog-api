from fastapi import APIRouter, HTTPException
from app.schemas.diary import DiaryCreateRequest, DiaryResponse
from app.services.llm import analyze_diary_text

router = APIRouter()
_fake_id = 0

@router.post("/diaries", response_model=DiaryResponse)
def create_diary(request: DiaryCreateRequest):
    """
    일기 생성 API (LLM 분석 포함 버전)
    """
    global _fake_id
    _fake_id += 1

    # 1) GPT로 분석
    try:
        result = analyze_diary_text(request.content)
    except Exception as e:
        # AI 호출 실패 시 500 에러로 알려주기
        raise HTTPException(status_code=500, detail=f"LLM error: {str(e)}")

    # 2) 필요한 키가 있는지 안전 체크
    for k in ("summary", "mood", "image_prompt"):
        if k not in result:
            raise HTTPException(status_code=500, detail=f"LLM response missing key: {k}")

    # 3) 응답 만들기
    return DiaryResponse(
        id=_fake_id,
        content=request.content,
        summary=result["summary"],
        mood=result["mood"],
        image_prompt=result["image_prompt"],
    )

@router.get("/diaries")
def list_diaries():
    return []
