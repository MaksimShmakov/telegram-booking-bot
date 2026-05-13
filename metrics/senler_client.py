"""Клиент Senler API. Реализуется на Этапе 1."""

from dataclasses import dataclass
from datetime import date


@dataclass
class SenlerMailing:
    mailing_id: int
    title: str
    sent_at: date
    sent: int
    delivered: int
    read: int
    cta_clicks: int   # клики по кнопке SENLER_CTA_BUTTON_TEXT


class SenlerClient:
    def __init__(self, api_token: str):
        self._token = api_token

    async def fetch_mailings(self, day: date) -> list[SenlerMailing]:
        raise NotImplementedError("этап 1")
