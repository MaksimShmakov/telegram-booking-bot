"""Запись метрик в Google Sheets. Реализуется на Этапе 4."""

from dataclasses import dataclass
from datetime import date


@dataclass
class MailingRow:
    day: date
    platform: str        # 'vk' | 'tg'
    channel: str         # имя канала Senler или бота Salebot
    mailing_id: str
    title: str
    grades: list[int]
    sent: int
    delivered: int
    read: int
    leads: int


class SheetsWriter:
    def __init__(self, credentials_path: str, sheet_id: str):
        self._creds = credentials_path
        self._sheet_id = sheet_id

    def append(self, rows: list[MailingRow]) -> None:
        """Идемпотентная запись: ключ (day, platform, channel, mailing_id)."""
        raise NotImplementedError("этап 4")
