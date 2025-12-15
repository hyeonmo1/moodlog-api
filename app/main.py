from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI
from app.api.routes.diaries import router as diary_router


app = FastAPI(
    title="MoodLog API",
)

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(diary_router, prefix="/api")