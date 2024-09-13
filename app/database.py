# app/database.py
from motor.motor_asyncio import AsyncIOMotorClient
from app.config import settings
from pydantic_settings import BaseSettings
from pydantic import Field
import asyncio

class Settings(BaseSettings):
    MONGODB_URI: str = Field(..., env="MONGODB_URI")
    DB_NAME: str = Field(..., env="DB_NAME")
    COLLECTION_NAME: str = Field(..., env="COLLECTION_NAME")
    APP_ENV: str = Field("development", env="APP_ENV")
    LOG_LEVEL: str = Field("info", env="LOG_LEVEL")

    class Config:
        env_file = ".env"  # This tells Pydantic to load variables from the .env file
        extra = "ignore"  # This tells Pydantic to ignore any extra variables that are not defined in the class

settings = Settings()

# # Example of accessing the settings
# print(settings.MONGODB_URI)
# print(settings.APP_ENV)

# Get or set event loop (explicitly defining the event loop)
loop = asyncio.get_event_loop()

# MongoDB connection
client = AsyncIOMotorClient(settings.MONGODB_URI, tlsAllowInvalidCertificates=True)
db = client[settings.DB_NAME]
problems_collection = db[settings.COLLECTION_NAME]

# Dependency to get the DB
def get_db():
    return problems_collection