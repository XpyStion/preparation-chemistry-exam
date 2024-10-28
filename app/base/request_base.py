from typing import Any

from requests import request, Response

AbstractRequestData = dict[str, Any]
AbstractHeaders = dict[str, str]
AbstractParams = dict[str, str]


class RequestBase(object):

    def __init__(self, base_url: str, timeout: int = 10, verify: bool = True) -> None:
        self.base_url = base_url
        self.timeout = timeout
        self.verify = verify

    def _make_request(
            self, method: str, endpoint: str,
            headers: AbstractHeaders = None, params: AbstractParams = None, data: AbstractRequestData = None, **kwargs
    ) -> Response:
        response = request(
            url=f'{self.base_url}/{endpoint}',
            method=method,
            headers=headers,
            params=params,
            json=data,
            timeout=self.timeout,
            verify=self.verify,
            **kwargs
        )
        response.raise_for_status()
        return response

    def get(self, endpoint: str, headers: AbstractHeaders = None, params: AbstractParams = None, **kwargs) -> Response:
        return self._make_request(method='GET', endpoint=endpoint, headers=headers, params=params, **kwargs)

    def post(self, endpoint: str, data: AbstractRequestData | None = None,
             headers: AbstractHeaders = None, params: AbstractParams = None, **kwargs
             ) -> Response:
        return self._make_request(method='POST', endpoint=endpoint, headers=headers, params=params, data=data, **kwargs)

    def put(self, endpoint: str, data: AbstractRequestData,
            headers: AbstractHeaders = None, params: AbstractParams = None, **kwargs
            ) -> Response:
        return self._make_request(method='PUT', endpoint=endpoint, headers=headers, params=params, data=data, **kwargs)

    def delete(self, endpoint: str,
               headers: AbstractHeaders = None, params: AbstractParams = None, **kwargs
               ) -> Response:
        return self._make_request(method='DELETE', endpoint=endpoint, headers=headers, params=params, **kwargs)
