from abc import ABC, abstractmethod
from functools import lru_cache

from app.api.yandex_gpt_api import YandexGPTAuthApi, YandexGPTApi


class GPTBase(ABC):

    @abstractmethod
    def get_prompt_response(self, **kwargs):
        pass


class YandexGPTClient(GPTBase):

    def __init__(
            self,
            token: str | None,
            folder_id: str | int | None,
    ) -> None:
        super().__init__()
        self.token = token
        self.folder_id = folder_id

        self._iam_token: str | None = None

    @property
    @lru_cache(maxsize=1)
    def iam_token(self) -> str:
        if self._iam_token is None:
            self._iam_token = YandexGPTAuthApi(token=self.token).post_iam_token().iamToken
        return self._iam_token

    def get_prompt_response(self, text: str, **kwargs) -> str:
        return YandexGPTApi(
            token=self._iam_token, folder_id=self.folder_id
        ).post_foundation_models_v1_completion(
            text=text, **kwargs
        ).result.alternatives[0].message.text
