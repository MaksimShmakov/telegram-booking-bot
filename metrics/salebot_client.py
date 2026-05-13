"""Клиент Salebot API. Реализуется на Этапе 2."""

from dataclasses import dataclass
from datetime import date


@dataclass
class SalebotMailing:
    project: str
    bot_id: str
    mailing_id: str
    title: str
    sent_at: date
    sent: int
    delivered: int
    read: int


class SalebotClient:
    def __init__(self, project: str, api_token: str):
        self.project = project
        self._token = api_token

    async def fetch_mailings(self, day: date) -> list[SalebotMailing]:
        raise NotImplementedError("этап 2")
