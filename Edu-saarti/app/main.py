from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import generate, lessons
# from app.routes import score  # You can uncomment this when score.py is ready

app = FastAPI(
    title="EduSetu Backend",
    description="API for generating multilingual lessons and quizzes from textbooks",
    version="0.1.0",
)

# CORS middleware to allow mobile app access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update with specific origins in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(generate.router, prefix="/api/v1")
app.include_router(lessons.router, prefix="/api/v1")
# app.include_router(score.router, prefix="/api/v1")  # Just skip this for now

@app.get("/")
async def root():
    return {"message": "Welcome to EduSetu Backend!"}
