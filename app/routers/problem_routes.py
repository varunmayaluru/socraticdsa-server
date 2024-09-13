# app/routers/problem_routes.py
from fastapi import APIRouter, Depends, HTTPException
from motor.motor_asyncio import AsyncIOMotorCollection
from app.models import Problem, ProblemSummary
from app.database import get_db
from typing import List
from app.services.problem_service import add_problem, get_problem_by_name, delete_problem_by_name, get_all_problems

router = APIRouter()

# add the default route 
@router.get("/")
async def read_root():
    return {"message": "Welcome to the Socratic DSA API!"}

# Route to add a new problem
@router.post("/problems")
async def create_problem(problem: Problem, db: AsyncIOMotorCollection = Depends(get_db)):
    problem_id = await add_problem(db, problem)
    return {"message": "Problem added successfully", "problem_id": problem_id}

# Route to get a problem by name (API-friendly name)
@router.get("/problems/{name}")
async def fetch_problem(name: str, db: AsyncIOMotorCollection = Depends(get_db)):
    # Query for the problem by name (case-insensitive)
    problem = await get_problem_by_name(db, name)
    if not problem:
        raise HTTPException(status_code=404, detail="Problem not found")
    return problem

# Route to delete a problem by name
@router.delete("/problems/{name}")
async def delete_problem(name: str, db: AsyncIOMotorCollection = Depends(get_db)):
    deleted = await delete_problem_by_name(db, name)
    if not deleted:
        raise HTTPException(status_code=404, detail="Problem not found")
    return {"message": f"Problem '{name}' deleted successfully."}

@router.get("/fetch-all-problems", response_model=List[ProblemSummary])
async def fetch_all_problems(db = Depends(get_db)):
    problems = await get_all_problems(db)
    if not problems:
        raise HTTPException(status_code=404, detail="No problems found")
    return problems