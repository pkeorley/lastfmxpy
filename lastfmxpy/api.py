# Copyright © 2023 pkeorley
#
# This source code is licensed under the MIT license found in the LICENSE
# file in the root directory of this source tree.

import requests
from aiohttp import ClientSession

from lastfmxpy.unions import (
    PostParam,
    PostMethod
)
from .utils import Utils


class BaseLastFMApi:
    def __init__(self, api_key: str, shared_secret: str):
        self._BASE_URL = "http://ws.audioscrobbler.com/2.0/"
        self._api_key = api_key
        self._shared_secret = shared_secret

    def _make_request(self, method, params, additional_params, async_request=False):
        if additional_params is None:
            additional_params = {"format": "json"}

        params_string = Utils.parse_params_by_json(params.to_json())
        additional_params_string = Utils.parse_params_by_json(additional_params)

        url = (
            f"{self._BASE_URL}?method={method.__str__()}"
            f"&api_key={self._api_key}"
            f"&{params_string}"
            f"{'&' if additional_params_string else ''}{additional_params_string}"
        )

        if async_request:
            return self._make_async_request(url)
        else:
            return self._make_sync_request(url)

    def _make_sync_request(self, url: str):
        response = requests.post(url, headers=Utils.get_headers())
        return response.text

    async def _make_async_request(self, url: str):
        async with ClientSession() as session:
            async with session.post(url, headers=Utils.get_headers()) as response:
                return await response.text()


class LastFMApi(BaseLastFMApi):
    def post(
            self,
            method: PostMethod,
            params: PostParam,
            additional_params: dict = None
    ) -> str:
        """
        A method that allows you to work with Last FM
        :param method: Method (you can find all methods in the documentation on the gitHub)
        :param params: Parameter (you can find all parameters in the documentation on the gitHub)
        :param additional_params: In the advanced settings, you can specify your own parameters
        :return: Returns a JSON or XML string (depending on additional parameters) with information
        """
        return self._make_request(
            method,
            params,
            additional_params
        )


class AsyncLastFMApi(BaseLastFMApi):
    async def post(
            self,
            method: PostMethod,
            params: PostParam,
            additional_params: dict = None
    ) -> str:
        """
        An asynchronous method that allows you to work with Last FM
        :param method: Method (you can find all methods in the documentation on the gitHub)
        :param params: Parameter (you can find all parameters in the documentation on the gitHub)
        :param additional_params: In the advanced settings, you can specify your own parameters
        :return: Returns a JSON or XML string (depending on additional parameters) with information
        """
        return await self._make_request(
            method,
            params,
            additional_params,
            async_request=True
        )
