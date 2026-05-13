# senler-salebot-metrics

Ежедневный сбор метрик рассылок из **Senler (ВК)** и **Salebot (Telegram)** с привязкой заявок из **AmoCRM** (через Postgres) и выгрузкой в **Google Sheets**.

## Что делает

Каждое утро в 07:00 (Мск) скрипт:

1. Идёт в Senler за рассылками всех ВК-каналов школы (15+ групп). Достаёт: отправлено / доставлено / прочитано / клики по «продажной» кнопке (по умолчанию — **«Узнать больше»**).
2. Идёт в Salebot за рассылками всех TG-ботов (4 проекта × N ботов). Достаёт: отправлено / доставлено / прочитано.
3. Тянет из **Postgres AmoCRM** заявки за дату с фильтром по источнику/тегу → раскладывает по рассылкам.
4. Парсит классы (9–11) из названий рассылок.
5. Пишет всё в Google Sheets идемпотентно (повторный запуск за ту же дату не дублирует строки).

## Структура

```
senler-salebot-metrics/
├── metrics/             # основной пакет
│   ├── senler_client.py     # Senler API
│   ├── salebot_client.py    # Salebot API
│   ├── amo_db.py            # Postgres → заявки AmoCRM
│   ├── classes.py           # парсер классов из названий
│   ├── sheets.py            # gspread → Google Sheets
│   ├── pipeline.py          # оркестрация: собрать → связать → записать
│   ├── scheduler.py         # APScheduler, cron 07:00
│   ├── channels.py          # справочник каналов и ботов
│   └── config.py            # настройки из .env
├── docs/
│   └── PLAN.md          # план этапов, договорённости, открытые вопросы
├── tests/
├── .env.example
├── requirements.txt
└── README.md
```

## Запуск (заглушка, в разработке)

```bash
cp .env.example .env  # заполнить ключи
pip install -r requirements.txt
python -m metrics              # одноразовый прогон за вчерашний день
python -m metrics --date 2026-05-12   # за конкретную дату
python -m metrics --daemon     # запустить с планировщиком
```

## Этап разработки

Сейчас: **Этап 0** — каркас и доступы. См. `docs/PLAN.md`.
