from pydantic import BaseModel, Field

class DiaryCreateRequest(BaseModel):    
    content: str = Field(..., description="일기 본문 텍스트.")


class DiaryResponse(BaseModel):
    id: int = Field(..., description="임시 일기 ID")  
    content: str = Field(..., description="일기 본문")
    summary: str = Field(..., description="일기 한줄 요약")
    mood: str = Field(..., description="일기 감정 분석 결과")
    import_prompt: str = Field(..., description="이미지 생성용 영어 프롬프트")