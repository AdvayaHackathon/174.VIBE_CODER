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
