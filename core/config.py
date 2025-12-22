import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "India Trade Insights API"
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "YOUR_KEY_HERE")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "super-secret-key-123")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

settings = Settings()