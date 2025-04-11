from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
<<<<<<< HEAD
from app.services.translator import translate_text
import json
import os

router = APIRouter()


LESSONS_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'lessons.json')

=======
from app.services.model_llama import generate_lesson
from app.services.translator import translate_and_tts

router = APIRouter()

>>>>>>> a2c5190c16f33e32ecca4803a8b16f90aef5141d
class GenerateRequest(BaseModel):
    grade: int
    subject: str
    topic: str
<<<<<<< HEAD
    language: str = "kn" 
=======
    language: str = "kn"  # Default to Kannada
>>>>>>> a2c5190c16f33e32ecca4803a8b16f90aef5141d

@router.post("/generate")
async def generate_content(request: GenerateRequest):
    try:
<<<<<<< HEAD
        
        with open(LESSONS_FILE, 'r', encoding='utf-8') as f:
            all_lessons = json.load(f)

        key = f"{request.grade}_{request.subject.lower()}_{request.topic.lower()}"
        if key not in all_lessons:
            raise HTTPException(status_code=404, detail="Lesson not found")

        lesson_data = all_lessons[key]
        lesson_content = lesson_data.get("lesson", "")
        quiz_content = lesson_data.get("quiz", [])

        if not isinstance(lesson_content, str) or not lesson_content.strip():
            raise HTTPException(status_code=500, detail="Lesson content is missing or invalid")

        # Translate the content
        translated_data = translate_content(
            content=lesson_content,
=======
        # Generate lesson and quiz using TinyLLaMA
        lesson_data = generate_lesson(
            grade=request.grade,
            subject=request.subject,
            topic=request.topic
        )

        # Translate and generate TTS using Sarvam AI
        translated_data = translate_and_tts(
            content=lesson_data,
>>>>>>> a2c5190c16f33e32ecca4803a8b16f90aef5141d
            target_language=request.language
        )

        return {
            "status": "success",
            "data": {
                "lesson": translated_data["lesson"],
<<<<<<< HEAD
                "quiz": quiz_content  # Optional: translate quiz later if needed
            }
        }

    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="Lesson data file not found")
=======
                "quiz": translated_data["quiz"],
                "tts_url": translated_data["tts_url"]
            }
        }
>>>>>>> a2c5190c16f33e32ecca4803a8b16f90aef5141d
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating content: {str(e)}")
