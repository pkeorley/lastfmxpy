# Copyright © 2023 pkeorley
#
# This source code is licensed under the MIT license found in the LICENSE
# file in the root directory of this source tree.

from enum import Enum
from typing import Type


class Library(Enum):
    GET_ARTISTS: str = "library.getArtists"

    def __str__(self) -> str:
        return self.value


def get_class() -> Type[Library]:
    return Library
