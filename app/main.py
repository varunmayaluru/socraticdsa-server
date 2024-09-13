# app/main.py
from fastapi import FastAPI
from app.routers import problem_routes, openai_routes
import os

app = FastAPI()

# Include the problem routes
app.include_router(problem_routes.router)
app.include_router(openai_routes.router)

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, loop="asyncio")
    # uvicorn.run(app, host="0.0.0.0", port=8000)
