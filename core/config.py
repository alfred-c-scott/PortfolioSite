# app/core/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    model_config = {
        "env_file": ".env"
    }

    name: str
    address: str
    phone: str
    email: str
    github: str

settings = Settings()