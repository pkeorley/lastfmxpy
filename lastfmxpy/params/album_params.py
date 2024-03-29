# Copyright © 2023 pkeorley
#
# This source code is licensed under the MIT license found in the LICENSE
# file in the root directory of this source tree.

import lastfmxpy.config as config
from lastfmxpy.exeptions import LFPPanic
from lastfmxpy.literals import Autocorrect
from lastfmxpy.params.base_classes import BaseAlbumParams
from lastfmxpy.utils import Utils


class AddTags(BaseAlbumParams):
    def __init__(
            self,
            artist: str,
            album: str,
            tags: list[str],
            api_key: str = None,
            api_sig: str = None,
            sk: str = None
    ):
        """
        Tag an album using a list of user supplied tags.
        :param artist: The artist name
        :param album: The album name
        :param tags: A comma delimited list of user supplied tags to apply to this album. Accepts a maximum of 10 tags.
        :param api_key: A Last.fm API key.
        :param api_sig: A Last.fm method signature. See authentication (https://www.last.fm/api/authentication) for more information.
        :param sk: A session key generated by authenticating a user via the authentication protocol.
        """
        super().__init__()

        if len(tags) > config.MAX_COUNT_OF_TAGS:
            raise LFPPanic(f"Accepts a maximum of 10 tags. You have {len(tags)}")

        self.artist = artist
        self.album = album
        self.tags = tags
        self.api_key = api_key
        self.api_sig = api_sig
        self.sk = sk

    def to_json(self) -> dict:
        return Utils.remove_none_values({
            "artist": self.artist,
            "album": self.album,
            "tags": ",".join(self.tags),
            "api_key": self.api_key,
            "api_sig": self.api_sig,
            "sk": self.sk
        })


class GetInfo(BaseAlbumParams):
    def __init__(
            self,
            artist: str = None,
            album: str = None,
            mbid: str = None,
            autocorrect: Autocorrect = None,
            username: str = None,
            lang: str = None,
            api_key: str = None
    ):
        """
        Get the metadata and tracklist for an album on Last.fm using the album name or a musicbrainz id.

        :param artist: The artist name
        :param album: The album name
        :param mbid: The musicbrainz id for the album
        :param autocorrect: Transform misspelled artist names into correct artist names, returning the correct version instead. The corrected artist name will be returned in the response.
        :param username: The username for the context of the request. If supplied, the user's playcount for this album is included in the response.
        :param lang: The language to return the biography in, expressed as an ISO 639 alpha-2 code.
        :param api_key: (optional) A Last.fm API key.
        """
        super().__init__()

        if not any((
            all((artist, album)),
            mbid
        )):
            raise LFPPanic("You must meet one of these conditions: fill in 'artist' and 'album' OR specify 'mbid'")

        self.artist = artist
        self.album = album
        self.mbid = mbid
        self.autocorrect = autocorrect
        self.username = username
        self.lang = lang
        self.api_key = api_key

    def to_json(self) -> dict:
        return Utils.remove_none_values({
            "artist": self.artist,
            "album": self.album,
            "mbid": self.mbid,
            "autocorrect": self.autocorrect,
            "username": self.username,
            "lang": self.lang,
            "api_key": self.api_key
        })


class GetTags(BaseAlbumParams):
    def __init__(
            self,
            artist: str = None,
            album: str = None,
            mbid: str = None,
            autocorrect: Autocorrect = None,
            user: str = None,
            api_key: str = None
    ):
        """
        Get the tags applied by an individual user to an album on Last.fm. To retrieve the list of top tags applied to an album by all users use album.getTopTags.
        :param artist: The artist name
        :param album: The album name
        :param mbid: The musicbrainz id for the album
        :param autocorrect:  Transform misspelled artist names into correct artist names, returning the correct version instead. The corrected artist name will be returned in the response.
        :param user: If called in non-authenticated mode you must specify the user to look up
        :param api_key: A Last.fm API key.
        """
        super().__init__()

        if not any((
                all((artist, album)),
                mbid
        )):
            raise LFPPanic("You must meet one of these conditions: fill in 'artist' and 'album' OR specify 'mbid'")

        self.artist = artist
        self.album = album
        self.mbid = mbid
        self.autocorrect = autocorrect
        self.user = user
        self.api_key = api_key

    def to_json(self) -> dict:
        return Utils.remove_none_values({
            "artist": self.artist,
            "album": self.album,
            "mbid": self.mbid,
            "autocorrect": self.autocorrect,
            "user": self.user,
            "api_key": self.api_key
        })


class GetTopTags(BaseAlbumParams):
    def __init__(
            self,
            artist: str = None,
            album: str = None,
            mbid: str = None,
            autocorrect: Autocorrect = None,
            api_key: str = None
    ):
        """
        Get the top tags for an album on Last.fm, ordered by popularity.
        :param artist: The artist name
        :param album: The album name
        :param mbid: The musicbrainz id for the album
        :param autocorrect: Transform misspelled artist names into correct artist names, returning the correct version instead. The corrected artist name will be returned in the response.
        :param api_key: A Last.fm API key.
        """
        super().__init__()

        if not any((
                all((artist, album)),
                mbid
        )):
            raise LFPPanic("You must meet one of these conditions: fill in 'artist' and 'album' OR specify 'mbid'")

        self.artist = artist
        self.album = album
        self.mbid = mbid
        self.autocorrect = autocorrect
        self.api_key = api_key

    def to_json(self) -> dict:
        return Utils.remove_none_values({
            "artist": self.artist,
            "album": self.album,
            "mbid": self.mbid,
            "autocorrect": self.autocorrect,
            "api_key": self.api_key
        })


class RemoveTag(BaseAlbumParams):
    def __init__(
            self,
            artist: str,
            album: str,
            tag: str,
            api_key: str = None,
            api_sig: str = None,
            sk: str = None
    ):
        """

        :param artist: The artist name
        :param album: The album name
        :param tag: A single user tag to remove from this album.
        :param api_key: A Last.fm API key.
        :param api_sig:  A Last.fm method signature. See authentication (https://www.last.fm/api/authentication) for more information.
        :param sk: A session key generated by authenticating a user via the authentication protocol.
        """
        super().__init__()

        self.artist = artist
        self.album = album
        self.tag = tag
        self.api_key = api_key
        self.api_sig = api_sig
        self.sk = sk

    def to_json(self) -> dict:
        return Utils.remove_none_values({
            "artist": self.artist,
            "album": self.album,
            "tag": self.tag,
            "api_key": self.api_key,
            "api_sig": self.api_sig,
            "sk": self.sk
        })


class Search(BaseAlbumParams):
    def __init__(
            self,
            limit: str | int,
            page: str | int,
            album: str,
            api_key: str
    ):
        """
        Search for an album by name. Returns album matches sorted by relevance.
        :param limit: The number of results to fetch per page. Defaults to 30
        :param page: The page number to fetch. Defaults to first page.
        :param album: The album name
        :param api_key: A Last.fm API key.
        """

        super().__init__()

        self.limit = limit
        self.page = page
        self.album = album
        self.api_key = api_key

    def to_json(self) -> dict:
        return Utils.remove_none_values({
            "limit": self.limit,
            "page": self.page,
            "album": self.album,
            "api_key": self.api_key
        })
