from app.api.models.yandex_gpt_api_models import PostIamTokenModel, PostFoundationModelsV1CompletionModel
from app.base.request_base import RequestBase, AbstractParams, AbstractHeaders
from app.constants import YANDEX_AUTH_URL, YANDEX_CLOUD_URL, YandexGPTModel


class YandexGPTAuthApi(RequestBase):

    def __init__(self, token: str | None, base_url: str = YANDEX_AUTH_URL):
        super().__init__(base_url)
        if not token:
            raise Exception

        self.token = token

    def post_iam_token(self) -> PostIamTokenModel:
        params: AbstractParams = {'yandexPassportOauthToken': self.token}
        response = self.post(endpoint='iam/v1/tokens', params=params)
        return PostIamTokenModel(**response.json())


class YandexGPTApi(RequestBase):

    def __init__(
            self,
            token: str | None,
            folder_id: str | None,
            base_url: str = YANDEX_CLOUD_URL,
    ):
        super().__init__(base_url)
        if not token or not folder_id:
            raise Exception

        self.token = token
        self.folder_id = folder_id

    @property
    def headers(self) -> AbstractHeaders:
        return {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}",
            "x-folder-id": self.folder_id

        }

    def post_foundation_models_v1_completion(
            self,
            text: str,
            role: str = "user",
            gpt_type: str = YandexGPTModel.YANDEXGPT_LITE,
            temperature: float = 0.3,
            max_tokens: int = 100
    ) -> PostFoundationModelsV1CompletionModel:
        data = {
            "modelUri": f"gpt://{self.folder_id}/{gpt_type}/rc",
            "completionOptions": {
                "stream": False,
                "temperature": temperature,
                "maxTokens": max_tokens
            },
            "messages": [{
                "role": role,
                "text": text
            }]
        }
        response = self.post(endpoint='foundationModels/v1/completion', data=data, headers=self.headers)
        return PostFoundationModelsV1CompletionModel(**response.json())
