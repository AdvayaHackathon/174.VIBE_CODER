from fastapi import APIRouter

router = APIRouter()  # This is mandatory!

@router.get("/lessons")
async def get_lessons():
    return {"message": "List of lessons"}