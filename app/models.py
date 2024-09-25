# app/models.py
from pydantic import BaseModel
from typing import List, Dict, Any, Union

# class Example(BaseModel):
#     input: Dict[str, Any]
#     output: float
#     explanation: str

class Example(BaseModel):
    input: str  # Input example, e.g., "nums1 = [1,3], nums2 = [2]"
    custom_input: Union[str, List]  # Customized input format for API processing
    # output: Union[float, List]  # The corresponding output of the example, can be a float or list
    output: str
    explanation: str  # Explanation for the result of the example

class Problem(BaseModel):
    name: str  # API-friendly name, e.g., "median_of_two_sorted_arrays"
    custom_name: str  # UI-friendly name, e.g., "Median of Two Sorted Arrays"
    difficulty: str  # Difficulty level of the problem, e.g., "Easy", "Medium", "Hard"
    description: str  # Full description of the problem
    examples: List[Example]  # A list of examples for the problem
    constraints: List[str]  # List of constraints as strings

class ProblemSummary(BaseModel):
    name: str
    custom_name: str
    difficulty: str

class CodeRequestModel(BaseModel):
    user_code: str  

class CodeResponseModel(BaseModel):
    combined_code: str  