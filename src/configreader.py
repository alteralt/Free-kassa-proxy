import pydantic

from pydantic_settings import BaseSettings


class Config(BaseSettings):
    notification_url: pydantic.HttpUrl
    success_url: pydantic.HttpUrl
    failure_url: pydantic.HttpUrl

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        env_nested_delimiter = "__"
