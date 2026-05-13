"""Postgres-доступ к данным AmoCRM. Реализуется на Этапе 2."""

from dataclasses import dataclass
from datetime import date


@dataclass
class AmoLead:
    lead_id: int
    created_at: date
    source: str           # 'senler' | 'salebot' | прочее
    mailing_ref: str | None  # как связали с конкретной рассылкой (utm/тег)


class AmoDB:
    def __init__(self, dsn: str):
        self._dsn = dsn

    async def fetch_leads(self, day: date) -> list[AmoLead]:
        raise NotImplementedError("этап 2")
