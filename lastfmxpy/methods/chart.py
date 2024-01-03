# Copyright © 2023 pkeorley
#
# This source code is licensed under the MIT license found in the LICENSE
# file in the root directory of this source tree.

from enum import Enum
from typing import Type


class Chart(Enum):
    GET_TOP_ARTISTS: str = "chart.getTopArtists"
    GET_TOP_TAGS: str = "chart.getTopTags"
    GET_TOP_TRACKS: str = "chart.getTopTracks"

    def __str__(self) -> str:
        return self.value


def get_class() -> Type[Chart]:
    return Chart
