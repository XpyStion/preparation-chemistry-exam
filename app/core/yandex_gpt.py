from abc import ABC, abstractmethod


class YandexGPTBase(ABC):

    @abstractmethod
    def exec_query(self):
        pass


class YandexGPT(YandexGPTBase):

    def get_iam_token(self):
        pass

    def exec_query(self):
        pass
