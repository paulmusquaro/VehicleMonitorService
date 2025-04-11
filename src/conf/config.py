from pathlib import Path
from pydantic_settings import BaseSettings
from pydantic import ConfigDict
import os

env_name = os.getenv("ENV_APP", "development")
base_dir = Path(__file__).resolve().parent
env_file_path = base_dir / f".env.{env_name}"

env_file = str(env_file_path) if env_file_path.exists() else None

class Settings(BaseSettings):
    ENV_APP: str = env_name
    DB_URL: str
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    model_config = ConfigDict(
        env_file=env_file,                    
        env_file_encoding="utf-8",            
        case_sensitive=True,
        extra="ignore"
    )

settings = Settings()