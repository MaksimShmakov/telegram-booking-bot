from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    senler_api_token: str = ""

    salebot_token_project_1: str = ""
    salebot_token_project_2: str = ""
    salebot_token_project_3: str = ""
    salebot_token_project_4: str = ""

    amo_pg_host: str = ""
    amo_pg_port: int = 5432
    amo_pg_db: str = ""
    amo_pg_user: str = ""
    amo_pg_password: str = ""

    google_credentials_path: str = "./service-account.json"
    gsheet_id: str = ""

    tz: str = "Europe/Moscow"
    alert_bot_token: str = ""
    alert_chat_id: str = ""

    @property
    def amo_pg_dsn(self) -> str:
        return (
            f"postgresql://{self.amo_pg_user}:{self.amo_pg_password}"
            f"@{self.amo_pg_host}:{self.amo_pg_port}/{self.amo_pg_db}"
        )


settings = Settings()
