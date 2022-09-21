from typing import Optional

from pydantic import BaseSettings, HttpUrl


class Config(BaseSettings):
    notification_url: HttpUrl
    success_url: HttpUrl
    failure_url: HttpUrl

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        env_nested_delimiter = "__"
