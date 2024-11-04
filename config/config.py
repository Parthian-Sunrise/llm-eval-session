from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    api_key: str

    model_config = SettingsConfigDict(
        env_prefix="OPENAI_",
        env_file="../.env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()


if __name__ == "__main__":
    print(settings.api_key)
