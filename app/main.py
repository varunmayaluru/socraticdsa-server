# app/main.py
from fastapi import FastAPI
from app.routers import problem_routes, openai_routes

app = FastAPI()

# Include the problem routes
app.include_router(problem_routes.router)
app.include_router(openai_routes.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, loop="asyncio")
