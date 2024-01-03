# Copyright © 2023 pkeorley
#
# This source code is licensed under the MIT license found in the LICENSE
# file in the root directory of this source tree.

from enum import Enum
from typing import Type


class Geo(Enum):
    GET_TOP_ARTISTS = "geo.getTopArtists"
    GET_TOP_TRACKS = "geo.getTopTracks"

    def __str__(self) -> str:
        return self.value


def get_class() -> Type[Geo]:
    return Geo
