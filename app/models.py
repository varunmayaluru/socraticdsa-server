# app/models.py
from pydantic import BaseModel
from typing import List, Dict, Any

class Example(BaseModel):
    input: Dict[str, Any]
    output: float
    explanation: str

class Problem(BaseModel):
    name: str  # API-friendly name, e.g., "median_of_two_sorted_arrays"
    custom_name: str  # UI-friendly name, e.g., "Median of Two Sorted Arrays"
    difficulty: str
    description: str
    examples: List[Example]
    constraints: List[str]

class ProblemSummary(BaseModel):
    name: str
    custom_name: str
    difficulty: str
