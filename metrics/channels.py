"""Справочник каналов и ботов. Заполняется на Этапе 0 вместе с Гришей."""

from dataclasses import dataclass


@dataclass(frozen=True)
class SenlerChannel:
    name: str           # человекочитаемое имя (для Sheets)
    vk_group_id: int    # id группы ВК
    subscription_id: int | None = None  # id подписки в Senler, если канал делится по подпискам


@dataclass(frozen=True)
class SalebotBot:
    project: str        # имя проекта Salebot
    bot_id: str         # id бота в проекте
    name: str           # человекочитаемое имя


# TODO(этап 0): заполнить после согласования с Гришей.
SENLER_CHANNELS: list[SenlerChannel] = []

SALEBOT_PROJECTS: dict[str, str] = {
    # project_name -> env var name with API token
    # "math_school":    "SALEBOT_TOKEN_PROJECT_1",
}

SALEBOT_BOTS: list[SalebotBot] = []

# Текст «продажной» кнопки в Senler-рассылках. Согласовано: 99% случаев.
SENLER_CTA_BUTTON_TEXT = "Узнать больше"
