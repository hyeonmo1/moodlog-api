import json
import os
from openai import OpenAI

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise RuntimeError("OPENAI_API_KEY is not set")

client = OpenAI(api_key=api_key)

SYSTEM_PROMPT = """
You are an emotion analysis assistant for a diary app called MoodLog.

Return ONLY valid JSON with keys:
- summary: 1 short Korean sentence (no quotes)
- mood: one of [Joy, Sadness, Anger, Anxiety, Calm, Hope]
- image_prompt: English prompt for a watercolor-style illustration (no text, no letters)

Rules:
- summary must be concise.
- mood must be exactly one of the allowed values.
- image_prompt should visualize the feeling and situation with warm, artistic details.

"""

def analyze_diary_text(text:str) -> dict:
    """
    입력: 일기 텍스트
    출력:{summary, mood, image_prompt} 딕셔너리

    """

    resp = client.chat.completions.create(
        model="gpt-4o-mini",   # 비용/속도 균형 좋은 모델(초기 개발용)
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": text},
        ],
        # JSON만 오게 강제(가능한 한 깔끔하게)
        response_format={"type": "json_object"},
        temperature=0.7,
    )

    content = resp.choices[0].message.content  
    return json.loads(content)