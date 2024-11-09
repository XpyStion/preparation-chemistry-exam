from os import getenv
from unittest import TestCase

from app.api.yandex_gpt_api import YandexGPTApi, YandexGPTAuthApi


class TestYandexGPTAuthApi(TestCase):

    def test_post_iam_token(self):
        # установить OAath-token в OAUTH-TOKEN
        token = getenv('OAUTH-TOKEN')
        self.assertTrue(YandexGPTAuthApi(token=token).post_iam_token().iamToken)


class TestYandexGPTApi(TestCase):

    def test_post_foundation_models_v1_completion(self):
        # установить OAath-token в OAUTH-TOKEN
        # установить folder id в FOLDER_ID
        token = getenv('OAUTH-TOKEN')
        folder_id = getenv('FOLDER_ID')
        iam_token = YandexGPTAuthApi(token=token).post_iam_token().iamToken

        text: str = '''
Дана формулировка задания:
"Для выполнения заданий 1−3 используйте следующий ряд химических элементов:
1. Be
2. F
3. Mg
4. Cl
5. Li
Ответом в заданиях 1−3 является последовательность цифр, под которыми указаны химические элементы в данном ряду.

Определите, какие из указанных элементов образуют положительный или отрицательный ион с электронной конфигурацией неона. Запишите в поле ответа номера выбранных элементов в порядке возрастания."
Напиши похожее задание за основу возьми шаблон формулировки
'''
        data = YandexGPTApi(token=iam_token, folder_id=folder_id).post_foundation_models_v1_completion(text=text)
        self.assertTrue(data.result.alternatives[0].message.text)
