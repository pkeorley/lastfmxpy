# Copyright © 2023 pkeorley
#
# This source code is licensed under the MIT license found in the LICENSE
# file in the root directory of this source tree.

from enum import Enum
from typing import Type


class Track(Enum):
    ADD_TAGS: str = "track.addTags"
    GET_CORRECTION: str = "track.getCorrection"
    GET_INFO: str = "track.getInfo"
    GET_SIMILAR: str = "track.getSimilar"
    GET_TAGS: str = "track.getTags"
    GET_TOP_TAGS: str = "track.getTopTags"
    LOVE: str = "track.love"
    REMOVE_TAG: str = "track.removeTag"
    SCROBBLE: str = "track.scrobble"
    SEARCH: str = "track.search"
    UNLOVE: str = "track.unlove"
    UPDATE_NOW_PLAYING: str = "track.updateNowPlaying"

    def __str__(self) -> str:
        return self.value


def get_class() -> Type[Track]:
    return Track
