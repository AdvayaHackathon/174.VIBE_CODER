from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.model_llama import generate_lesson
from app.services.translator import translate_and_tts

router = APIRouter()

class GenerateRequest(BaseModel):
    grade: int
    subject: str
    topic: str
    language: str = "kn"  # Default to Kannada

@router.post("/generate")
async def generate_content(request: GenerateRequest):
    try:
        # Generate lesson and quiz using TinyLLaMA
        lesson_data = generate_lesson(
            grade=request.grade,
            subject=request.subject,
            topic=request.topic
        )

        # Translate and generate TTS using Sarvam AI
        translated_data = translate_and_tts(
            content=lesson_data,
            target_language=request.language
        )

        return {
            "status": "success",
            "data": {
                "lesson": translated_data["lesson"],
                "quiz": translated_data["quiz"],
                "tts_url": translated_data["tts_url"]
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating content: {str(e)}")
