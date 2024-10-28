import os
from unittest import TestCase

from app.core.gpt import YandexGPTClient


class TestYandexGPT(TestCase):

    def test_exec(self):
        YandexGPTClient(iam_token=os.getenv('IAM_TOKEN'), catalog_id=os.getenv('CATALOG_ID')).exec()
