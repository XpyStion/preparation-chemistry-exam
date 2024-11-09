from os import getenv
from unittest import TestCase

from app.api.yandex_gpt_api import YandexGPTAuthApi
from app.core.yandex_gpt_client import YandexGPTClient


class TestYandexGPT(TestCase):

    def test_get_prompt_response_msg(self):
        # установить OAath-token в OAUTH-TOKEN
        # установить folder id в FOLDER_ID
        token = getenv('OAUTH_TOKEN')
        folder_id = getenv('FOLDER_ID')

        text: str = 'Ответь сколько дней в году?'
        self.assertTrue(YandexGPTClient(token=token, folder_id=folder_id).get_prompt_response_msg(text=text))
