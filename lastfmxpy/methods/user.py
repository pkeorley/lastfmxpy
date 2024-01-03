# Copyright © 2023 pkeorley
#
# This source code is licensed under the MIT license found in the LICENSE
# file in the root directory of this source tree.

from enum import Enum
from typing import Type


class User(Enum):
    GET_FRIENDS: str = "user.getFriends"
    GET_INFO: str = "user.getInfo"
    GET_LOVED_TRACKS: str = "user.getLovedTracks"
    GET_PERSONAL_TAGS: str = "user.getPersonalTags"
    GET_RECENT_TRACKS: str = "user.getRecentTracks"
    GET_TOP_ALBUMS: str = "user.getTopAlbums"
    GET_TOP_ARTISTS: str = "user.getTopArtists"
    GET_TOP_TAGS: str = "user.getTopTags"
    GET_TOP_TRACKS: str = "user.getTopTracks"
    GET_WEEKLY_ALBUM_CHART: str = "user.getWeeklyAlbumChart"
    GET_WEEKLY_ARTIST_CHART: str = "user.getWeeklyArtistChart"
    GET_WEEKLY_CHART_LIST: str = "user.getWeeklyChartList"
    GET_WEEKLY_TRACK_CHART: str = "user.getWeeklyTrackChart"

    def __str__(self) -> str:
        return self.value


def get_class() -> Type[User]:
    return User
