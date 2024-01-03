# Copyright © 2023 pkeorley
#
# This source code is licensed under the MIT license found in the LICENSE
# file in the root directory of this source tree.

from enum import Enum
from typing import Type


class Tag(Enum):
    GET_INFO: str = "tag.getInfo"
    GET_SIMILAR: str = "tag.getSimilar"
    GET_TOP_ALBUMS: str = "tag.getTopAlbums"
    GET_TOP_ARTISTS: str = "tag.getTopArtists"
    GET_TOP_TAGS: str = "tag.getTopTags"
    GET_TOP_TRACKS: str = "tag.getTopTracks"
    GET_WEEKLY_CHART_LIST: str = "tag.getWeeklyChartList"

    def __str__(self) -> str:
        return self.value


def get_class() -> Type[Tag]:
    return Tag
