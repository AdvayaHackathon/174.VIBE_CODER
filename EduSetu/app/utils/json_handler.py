import json
from pathlib import Path

DATA_PATH = Path(__file__).parent.parent / "data" / "lessons.json"

def load_lessons():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def save_lessons(data):
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
