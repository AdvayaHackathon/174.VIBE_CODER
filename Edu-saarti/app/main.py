# ~/Edu-saarti/app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import lessons

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
app.include_router(lessons.router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "EduSetu Backend"}