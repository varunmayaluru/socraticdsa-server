# app/models.py
from pydantic import BaseModel
from typing import List, Dict, Any

class Example(BaseModel):
    input: Dict[str, Any]
    output: float
    explanation: str

class Example(BaseModel):
    input: str  # Input example, e.g., "nums1 = [1,3], nums2 = [2]"
    output: float  # The corresponding output of the example
    explanation: str  # Explanation for the result of the example

class Problem(BaseModel):
    name: str  # API-friendly name, e.g., "median_of_two_sorted_arrays"
    custom_name: str  # UI-friendly name, e.g., "Median of Two Sorted Arrays"
    difficulty: str
    description: str
    examples: List[Example]  # A list of examples for the problem
    constraints: List[str]  # List of constraints as strings

class ProblemSummary(BaseModel):
    name: str
    custom_name: str
    difficulty: str
