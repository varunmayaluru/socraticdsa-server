import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MONGODB_URI: str = os.getenv("MONGODB_URI", "mongodb+srv://socraticdsa:socraticdsa@socraticdsa.x4l8y.mongodb.net/?retryWrites=true&w=majority&appName=socraticdsa")
    DB_NAME: str = "socraticdsa"
    COLLECTION_NAME: str = "sorting_algo"
    APP_ENV: str = os.getenv("APP_ENV", "development")
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "info")

settings = Settings()
