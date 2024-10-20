import logging

from pydantic import AnyUrl
from pydantic_settings import BaseSettings
from functools import lru_cache


log = logging.getLogger("uvicorn")

class Settings(BaseSettings):
    """Configuration settings for the application."""

    environment: str = "dev"
    testing: bool = bool(0)
    database_url: AnyUrl = None
 
@lru_cache()
def get_settings() -> BaseSettings:
    log.info("Loading config settings from the environment...")
    return Settings()