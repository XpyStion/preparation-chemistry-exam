from os import getenv
from unittest import TestCase

from app.api.yandex_gpt_api import YandexGPTAuthApi
from app.core.yandex_gpt_client import YandexGPTClient


class TestYandexGPT(TestCase):

    def test_exec(self):
        # установить OAath-token в OAUTH-TOKEN
        # установить folder id в FOLDER_ID
        token = getenv('OAUTH-TOKEN')
        folder_id = getenv('FOLDER_ID')
        iam_token = YandexGPTAuthApi(token=token).post_iam_token().iamToken

        text: str = 'Ответь сколько дней в году?'
        self.assertTrue(YandexGPTClient(token=iam_token, folder_id=folder_id).get_prompt_response(text=text))
