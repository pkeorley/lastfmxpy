# Copyright © 2023 pkeorley
#
# This source code is licensed under the MIT license found in the LICENSE
# file in the root directory of this source tree.

import requests

from .methods import (
    Album,
    Artist,
    Auth,
    Chart,
    Geo,
    Library,
    Tag,
    Track,
    User
)
from .params.base_classes import (
    BaseAlbumParams,
    BaseArtistParams,
    BaseAuthParams,
    BaseChartParams,
    BaseGeoParams,
    BaseLibraryParams,
    BaseTagParams,
    BaseTrackParams,
    BaseUserParams
)
from .utils import Utils


class LastFMApi:
    def __init__(
            self,
            api_key: str,
            shared_secret: str
    ):
        """
        The class through which requests will be sent (Get your api key and shared key here https://www.last.fm/api/account/create)
        :param api_key: A Last.fm API key
        :param shared_secret: A Shared Secret
        """
        self._BASE_URL = "http://ws.audioscrobbler.com/2.0/"
        self._api_key = api_key
        self._shared_secret = shared_secret

    def post(
            self,
            method: Album | Artist | Auth | Chart | Geo | Library | Tag | Track | User,
            params: BaseAlbumParams | BaseArtistParams | BaseAuthParams | BaseChartParams | BaseGeoParams | BaseLibraryParams | BaseTagParams | BaseTrackParams | BaseUserParams,
            additional_params: dict = None
    ) -> str:
        """
        A method that allows you to work with Last FM
        :param method: Method (you can find all methods in the documentation on the gitHub)
        :param params: Parameter (you can find all parameters in the documentation on the gitHub)
        :param additional_params: In the advanced settings, you can specify your own parameters
        :return: Returns a JSON or XML string (depending on additional parameters) with information
        """

        if additional_params is None:
            additional_params = {
                "format": "json"
            }

        params_string = Utils.parse_params_by_json(params.to_json())
        additional_params_string = Utils.parse_params_by_json(additional_params)

        url = (
            f"{self._BASE_URL}?method={method.__str__()}"
            f"&api_key={self._api_key}"
            f"&{params_string}"
            f"{'&' if additional_params_string else ''}{additional_params_string}"
        )

        response = requests.post(
            url,
            headers=Utils.get_headers()
        )

        return response.text
