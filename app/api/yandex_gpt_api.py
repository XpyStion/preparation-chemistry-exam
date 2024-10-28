from os import getenv

from app.base.request_base import RequestBase, AbstractParams
from app.constants import YANDEX_GPT_URL


class YandexGPTApi(RequestBase):

    def __init__(self, base_url: str = YANDEX_GPT_URL, token: str | None = getenv('API_KEY')):
        super().__init__(base_url)
        if not token:
            raise Exception

        self.token = token
        self.api_uri = ''

    def post_iam_token(self) -> dict[str, str]:
        params: AbstractParams = {'yandexPassportOauthToken': self.token}
        response = self.post(endpoint='iam/v1/tokens', params=params)
        return response.json()
