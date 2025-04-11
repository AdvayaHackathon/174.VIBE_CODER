<<<<<<< HEAD

from fastapi import APIRouter, HTTPException
import json  
import os
from app.services.translator import translate_text

router = APIRouter()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LESSONS_PATH = os.path.join(BASE_DIR, "data", "lessons.json")

def load_lessons():
    if not os.path.exists(LESSONS_PATH):
        raise FileNotFoundError(f"Lessons file not found at {LESSONS_PATH}")
    with open(LESSONS_PATH, "r") as f:
        return json.load(f)

@router.get("/generate")
async def generate(grade: int, subject: str, topic: str, language: str = "kn"):
    try:
        lessons = load_lessons()
        for lesson in lessons:
            if (lesson["grade"] == grade and 
                lesson["subject"] == subject and 
                lesson["topic"] == topic):
                lesson_text = lesson["lesson"]
                quiz = lesson["quiz"]

                if language != "en":
                    translated_lesson = translate_text(lesson_text, f"{language}-IN")
                else:
                    translated_lesson = lesson_text

                return {
                    "status": "success",
                    "data": {
                        "lesson": translated_lesson,
                        "quiz": quiz,
                        "tts_url": None
                    }
                }
        return {"status": "error", "message": "Topic not found"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
=======
from fastapi import APIRouter

router = APIRouter()  # This is mandatory!

@router.get("/lessons")
async def get_lessons():
    return {"message": "List of lessons"}
>>>>>>> a2c5190c16f33e32ecca4803a8b16f90aef5141d
