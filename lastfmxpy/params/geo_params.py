# Copyright © 2023 pkeorley
#
# This source code is licensed under the MIT license found in the LICENSE
# file in the root directory of this source tree.

from lastfmxpy.params.base_classes import BaseGeoParams
from lastfmxpy.utils import Utils


class GetTopArtists(BaseGeoParams):
    def __init__(
            self,
            country: str,
            page: str | int = None,
            limit: str | int = None,
            api_key: str = None
    ):
        """
        Get the most popular artists on Last.fm by country
        :param country: A country name, as defined by the ISO 3166-1 country names standard
        :param page: The page number to fetch. Defaults to first page.
        :param limit: The number of results to fetch per page. Defaults to 50.
        :param api_key: A Last.fm API key.
        """
        super().__init__()

        self.country = country
        self.page = page
        self.limit = limit
        self.api_key = api_key

    def to_json(self) -> dict:
        return Utils.remove_none_values({
            "country": self.country,
            "page": self.page,
            "limit": self.limit,
            "api_key": self.api_key
        })


class GetTopTracks(BaseGeoParams):
    def __init__(
            self,
            country: str,
            location: str = None,
            page: str | int = None,
            limit: str | int = None,
            api_key: str = None
    ):
        """
        Get the most popular tracks on Last.fm last week by country
        :param country: A country name, as defined by the ISO 3166-1 country names standard
        :param location: A metro name, to fetch the charts for (must be within the country specified)
        :param page: The page number to fetch. Defaults to first page.
        :param limit: The number of results to fetch per page. Defaults to 50.
        :param api_key: A Last.fm API key.
        """
        super().__init__()

        self.country = country
        self.location = location
        self.page = page
        self.limit = limit
        self.api_key = api_key

    def to_json(self) -> dict:
        return Utils.remove_none_values({
            "country": self.country,
            "location": self.location,
            "page": self.page,
            "limit": self.limit,
            "api_key": self.api_key
        })
