from unittest import TestCase

from app.api.yandex_gpt_api import YandexGPTApi, YandexGPTAuthApi


class TestYandexGPTAuthApi(TestCase):

    def test_post_iam_token(self):
        # установить OAath-token в OAUTH-TOKEN
        self.assertTrue(YandexGPTAuthApi().post_iam_token().iamToken)


class TestYandexGPTApi(TestCase):
    def test_post_foundation_models_v1_completion(self):
        # установить OAath-token в OAUTH-TOKEN
        # установить folder id в FOLDER_ID
        iam_token = YandexGPTAuthApi().post_iam_token().iamToken

        text: str = 'Ответь сколько дней в году?'
        data = YandexGPTApi(token=iam_token).post_foundation_models_v1_completion(text=text)
        self.assertTrue(data.result.alternatives[0].message.text)
