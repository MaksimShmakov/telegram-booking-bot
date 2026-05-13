"""Точка входа: `python -m metrics`."""

import argparse
import asyncio
from datetime import date

from metrics.pipeline import run_for_day, yesterday
from metrics.scheduler import run_daemon


def main() -> None:
    parser = argparse.ArgumentParser(prog="metrics")
    parser.add_argument("--date", type=date.fromisoformat, default=None,
                        help="дата в формате YYYY-MM-DD; по умолчанию — вчера")
    parser.add_argument("--daemon", action="store_true",
                        help="запустить с планировщиком (cron 07:00)")
    args = parser.parse_args()

    if args.daemon:
        run_daemon()
        return

    day = args.date or yesterday()
    asyncio.run(run_for_day(day))


if __name__ == "__main__":
    main()
