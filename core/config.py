from functools import lru_cache
from typing import Optional
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    gemini_api_key: str = ""
    telegram_bot_token: str = ""
    telegram_chat_id: str = ""
    admin_pass: Optional[str] = None
    secret_key: Optional[str] = None
    db_path: str = "data/veritas_eleitoral.db"
    portal_transparencia_api_key: str = ""


@lru_cache
def get_settings() -> Settings:
    return Settings()
