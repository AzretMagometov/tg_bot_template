from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import URL


class EnvBaseSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")


class BotSettings(EnvBaseSettings):
    BOT_TOKEN: str


class CacheSettings(EnvBaseSettings):
    REDIS_HOST: str = "redis"
    REDIS_PORT: int = 6379
    REDIS_PASS: str | None = None

    @property
    def redis_url(self) -> str:
        if self.REDIS_PASS:
            return f"redis://{self.REDIS_PASS}@{self.REDIS_HOST}:{self.REDIS_PORT}/0"
        return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}/0"


class DatabaseSettings(EnvBaseSettings):
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_USER: str = "postgres"
    DB_PASS: str | None = None
    DB_NAME: str = "postgres"

    @property
    def database_url(self) -> URL | str:
        if self.DB_PASS:
            return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        return f"postgresql+asyncpg://{self.DB_USER}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


class ProxySettings(EnvBaseSettings):
    PROXY_HOST: str
    PROXY_PORT: int
    PROXY_LOGIN: str
    PROXY_PASSWORD: str

    @property
    def proxy(self) -> str:
        return f'http://{self.PROXY_LOGIN}:{self.PROXY_PASSWORD}@{self.PROXY_HOST}:{self.PROXY_PORT}'


class Settings(BotSettings, CacheSettings, DatabaseSettings, ProxySettings):
    DEBUG: bool = True
    RATE_LIMIT: int | float = 0.5


settings = Settings()
