# Copyright © 2023 pkeorley
#
# This source code is licensed under the MIT license found in the LICENSE
# file in the root directory of this source tree.

from enum import Enum
from typing import Type


class Artist(Enum):
    ADD_TAGS: str = "artist.addTags"
    GET_CORRECTION: str = "artist.getCorrection"
    GET_INFO: str = "artist.getInfo"
    GET_SIMILAR: str = "artist.getSimilar"
    GET_TAGS: str = "artist.getTags"
    GET_TOP_ALBUMS: str = "artist.getTopAlbums"
    GET_TOP_TAGS: str = "artist.getTopTags"
    GET_TOP_TRACKS: str = "artist.getTopTracks"
    REMOVE_TAG: str = "artist.removeTag"
    SEARCH: str = "artist.search"

    def __str__(self) -> str:
        return self.value


def get_class() -> Type[Artist]:
    return Artist
