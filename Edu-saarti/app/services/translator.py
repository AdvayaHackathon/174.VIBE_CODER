
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