<<<<<<< HEAD

import os
import requests
import json  
from dotenv import load_dotenv
from fastapi import HTTPException

load_dotenv()
SARVAM_API_KEY = os.getenv("SARVAM_API_KEY", "").strip()

def translate_text(text: str, target_language_code: str, source_language_code: str = "en-IN") -> str:
    if not SARVAM_API_KEY:
        return f"[Mock {target_language_code}] {text}"

    url = "https://api.sarvam.ai/translate"
    headers = {
        "API-Subscription-Key": SARVAM_API_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "input": text,
        "source_language_code": source_language_code,
        "target_language_code": target_language_code
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload), timeout=30)
        response.raise_for_status()
        result = response.json()
        return result.get("translated_text", text)
    except requests.exceptions.RequestException as e:
        print(f"Translation error: {e}")
        return f"[Mock {target_language_code}] {text}"
=======
import os
import requests
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment
api_key = os.getenv("SARVAM_API_KEY")

if not api_key:
    raise Exception("❌ SARVAM_API_KEY is missing in your .env file")

translation_url = "https://api.sarvam.ai/translate"

headers = {
    "API-Subscription-Key": api_key,
    "Content-Type": "application/json"
}

def translate_text(text: str, target_language: str) -> str:
    payload = {
        "input": text,
        "source_language_code": "en-IN",
        "target_language_code": f"{target_language}-IN"
    }

    response = requests.post(translation_url, headers=headers, data=json.dumps(payload))
    if response.status_code == 200:
        result = response.json()
        translated_text = result.get("translated_text") or result.get("text") or result.get("output")
        return translated_text
    else:
        raise Exception(f"Translation failed: {response.status_code}, {response.text}")

def generate_tts(text: str, language: str) -> str:
    # Placeholder for TTS logic
    return f"https://dummy.tts.service/{language}/audio.mp3"

def translate_and_tts(content: str, target_language: str):
    translated = translate_text(content, target_language)
    tts_url = generate_tts(translated, target_language)

    return {
        "lesson": translated,
        "quiz": "Quiz generation not separated yet.",
        "tts_url": tts_url
    }
>>>>>>> a2c5190c16f33e32ecca4803a8b16f90aef5141d
