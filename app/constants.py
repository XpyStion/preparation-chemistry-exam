from enum import Enum

YANDEX_AUTH_URL: str = 'https://iam.api.cloud.yandex.net'
YANDEX_CLOUD_URL: str = 'https://llm.api.cloud.yandex.net'


class YandexGPTModel(str, Enum):
    YANDEXGPT: str = 'yandexgpt'
    YANDEXGPT_LITE: str = 'yandexgpt-lite'
    SUMMARIZATION: str = 'summarization'

    def __str__(self) -> str:
        return str.__str__(self)
