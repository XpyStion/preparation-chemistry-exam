from abc import ABC, abstractmethod

from yandex_gpt import YandexGPT, YandexGPTConfigManagerBase

from app.api.yandex_gpt_api import YandexGPTApi
from app.constants import YandexGPTModel


class GPTBase(ABC):

    @abstractmethod
    def exec(self):
        pass


class YandexGPTClient(GPTBase):

    def __init__(
            self,
            catalog_id: str | int,
            model: str = YandexGPTModel.YANDEXGPT,
            iam_token: str | None = None,
            api_key: str | None = None,
    ) -> None:
        super().__init__()
        self.yandex_gpt_api = YandexGPTApi(token=api_key)

        if api_key is None and iam_token is None:
            raise Exception

        settings = YandexGPTConfigManagerBase(
            model_type=model,
            catalog_id=catalog_id,
            iam_token=self.get_iam_token(),
            api_key=api_key
        )
        self.gpt = YandexGPT(settings)

    def get_iam_token(self) -> str:
        return self.yandex_gpt_api.post_iam_token().get("iamToken")

    def exec(self):
        x = self.gpt.get_sync_completion(messages=[{"role": "user", "text": "Hello, world!"}])
        print(x)

