from pydantic_settings import BaseSettings, SettingsConfigDict
from src.utils.config import env_file_path
from typing import Annotated
from pydantic import Field


class TeleConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file=env_file_path, extra="ignore")

    bot_token: Annotated[str, Field(..., description="Токен для аутентификации бота.")]
