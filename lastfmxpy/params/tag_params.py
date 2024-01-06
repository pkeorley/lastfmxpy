# Copyright © 2023 pkeorley
#
# This source code is licensed under the MIT license found in the LICENSE
# file in the root directory of this source tree.

from lastfmxpy.params.base_classes import BaseTagParams
from lastfmxpy.utils import Utils


class GetInfo(BaseTagParams):
    def __init__(
            self,
            tag: str,
            lang: str = None,
            api_key: str = None
    ):
        """
        Search for tags similar to this one. Returns tags ranked by similarity, based on listening data.
        :param tag: The tag name
        :param lang: The language to return the wiki in, expressed as an ISO 639 alpha-2 code.
        :param api_key:  A Last.fm API key.
        """
        super().__init__()

        self.tag = tag
        self.lang = lang
        self.api_key = api_key

    def to_json(self) -> dict:
        return Utils.remove_none_values({
            "tag": self.tag,
            "lang": self.lang,
            "api_key": self.api_key
        })


class GetSimilar(BaseTagParams):
    def __init__(
            self,
            tag: str,
            api_key: str = None
    ):
        """
        Search for tags similar to this one. Returns tags ranked by similarity, based on listening data.
        :param tag: The tag name
        :param api_key:  A Last.fm API key.
        """
        super().__init__()

        self.tag = tag
        self.api_key = api_key

    def to_json(self) -> dict:
        return Utils.remove_none_values({
            "tag": self.tag,
            "api_key": self.api_key
        })


class GetTopAlbums(BaseTagParams):
    def __init__(
            self,
            tag: str,
            limit: str | int = None,
            page: str | int = None,
            api_key: str = None
    ):
        """
        Get the top albums tagged by this tag, ordered by tag count.
        :param tag: The tag name
        :param limit: The number of results to fetch per page. Defaults to 50.
        :param page: The page number to fetch. Defaults to first page.
        :param api_key:  A Last.fm API key.
        """
        super().__init__()

        self.tag = tag
        self.limit = limit
        self.page = page
        self.api_key = api_key

    def to_json(self) -> dict:
        return Utils.remove_none_values({
            "tag": self.tag,
            "limit": self.limit,
            "page": self.page,
            "api_key": self.api_key
        })


class GetTopArtists(BaseTagParams):
    def __init__(
            self,
            tag: str,
            limit: str | int = None,
            page: str | int = None,
            api_key: str = None
    ):
        """
        Get the top artists tagged by this tag, ordered by tag count.
        :param tag: The tag name
        :param limit: The number of results to fetch per page. Defaults to 50.
        :param page: The page number to fetch. Defaults to first page.
        :param api_key:  A Last.fm API key.
        """
        super().__init__()

        self.tag = tag
        self.limit = limit
        self.page = page
        self.api_key = api_key

    def to_json(self) -> dict:
        return Utils.remove_none_values({
            "tag": self.tag,
            "limit": self.limit,
            "page": self.page,
            "api_key": self.api_key
        })


class GetTopTags(BaseTagParams):
    def __init__(
            self,
            api_key: str = None
    ):
        """
        Fetches the top global tags on Last.fm, sorted by popularity (number of times used)
        :param api_key: A Last.fm API key.
        """
        super().__init__()

        self.api_key = api_key

    def to_json(self) -> dict:
        return Utils.remove_none_values({
            "api_key": self.api_key
        })


class GetTopTracks(BaseTagParams):
    def __init__(
            self,
            tag: str,
            limit: str | int = None,
            page: str | int = None,
            api_key: str = None
    ):
        """
        Get the top tracks tagged by this tag, ordered by tag count.
        :param tag: The tag name
        :param limit: The number of results to fetch per page. Defaults to 50.
        :param page: The page number to fetch. Defaults to first page.
        :param api_key:  A Last.fm API key.
        """
        super().__init__()

        self.tag = tag
        self.limit = limit
        self.page = page
        self.api_key = api_key

    def to_json(self) -> dict:
        return Utils.remove_none_values({
            "tag": self.tag,
            "limit": self.limit,
            "page": self.page,
            "api_key": self.api_key
        })


class GetWeeklyChartList(BaseTagParams):
    def __init__(
            self,
            tag: str,
            api_key: str
    ):
        super().__init__()

        self.tag = tag
        self.api_key = api_key

    def to_json(self) -> dict:
        return Utils.remove_none_values({
            "tag": self.tag,
            "api_key": self.api_key
        })
