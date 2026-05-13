"""Оркестратор: собрать данные из всех источников за день и записать в Sheets."""

from datetime import date, timedelta


async def run_for_day(day: date) -> None:
    """Однократный прогон пайплайна за указанную дату.

    Реализация добавляется поэтапно:
      этап 1 → Senler
      этап 2 → Salebot + AmoCRM
      этап 3 → нормализация классов
      этап 4 → запись в Sheets
    """
    raise NotImplementedError("этапы 1–4")


def yesterday() -> date:
    return date.today() - timedelta(days=1)
