import os
import httpx
from dotenv import load_dotenv
from typing import Tuple
import re

# Load environment variables from .env file
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_API_URL = "https://api.openai.com/v1/chat/completions"

async def fetch_openai_response(messages: list) -> dict:
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }

    # Convert the list of Message objects to a list of dictionaries
    messages_dict = [message.dict() for message in messages]

    data = {
        "model": "gpt-4",
        "messages": messages_dict
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(OPENAI_API_URL, headers=headers, json=data)
        response.raise_for_status()
        return response.json()

def parse_openai_response(response: dict) -> Tuple[str, str]:
    content = response['choices'][0]['message']['content']
    
    # Regex to find code blocks enclosed by triple backticks
    code_blocks = re.findall(r"```(.*?)```", content, re.DOTALL)
    code_output = "\n".join(code_blocks)
    
    # Remove code blocks from the content to get the text output
    text_output = re.sub(r"```.*?```", "", content, flags=re.DOTALL).strip()
    
    return text_output, code_output
