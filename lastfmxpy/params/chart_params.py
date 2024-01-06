# Copyright © 2023 pkeorley
#
# This source code is licensed under the MIT license found in the LICENSE
# file in the root directory of this source tree.

from lastfmxpy.params.base_classes import BaseChartParams
from lastfmxpy.utils import Utils


class GetTopArtists(BaseChartParams):
    def __init__(
            self,
            page: str | int = None,
            limit: str | int = None,
            api_key: str = None
    ):
        """
        Get the top artists chart
        :param page: The page number to fetch. Defaults to first page.
        :param limit: The number of results to fetch per page. Defaults to 50.
        :param api_key: A Last.fm API key.
        """
        super().__init__()

        self.page = page
        self.limit = limit
        self.api_key = api_key

    def to_json(self) -> dict:
        return Utils.remove_none_values({
            "page": self.page,
            "limit": self.limit,
            "api_key": self.api_key
        })


class GetTopTags(BaseChartParams):
    def __init__(
            self,
            page: str | int = None,
            limit: str | int = None,
            api_key: str = None
    ):
        """
        Get the top artists chart
        :param page: The page number to fetch. Defaults to first page.
        :param limit: The number of results to fetch per page. Defaults to 50.
        :param api_key: A Last.fm API key.
        """
        super().__init__()

        self.page = page
        self.limit = limit
        self.api_key = api_key

    def to_json(self) -> dict:
        return Utils.remove_none_values({
            "page": self.page,
            "limit": self.limit,
            "api_key": self.api_key
        })


class GetTopTracks(BaseChartParams):
    def __init__(
            self,
            page: str | int = None,
            limit: str | int = None,
            api_key: str = None
    ):
        """
        Get the top tracks chart
        :param page: The page number to fetch. Defaults to first page.
        :param limit: The number of results to fetch per page. Defaults to 50.
        :param api_key: A Last.fm API key.
        """
        super().__init__()

        self.page = page
        self.limit = limit
        self.api_key = api_key

    def to_json(self) -> dict:
        return Utils.remove_none_values({
            "page": self.page,
            "limit": self.limit,
            "api_key": self.api_key
        })
