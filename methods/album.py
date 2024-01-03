# Copyright © 2023 pkeorley
#
# This source code is licensed under the MIT license found in the LICENSE
# file in the root directory of this source tree.

from enum import Enum
from typing import Type


class Album(Enum):
    ADD_TAGS: str = "album.addTags"
    GET_INFO: str = "album.getInfo"
    GET_TAGS: str = "album.getTags"
    GET_TOP_TAGS: str = "album.getTopTags"
    REMOVE_TAG: str = "album.removeTag"
    SEARCH: str = "album.search"

    def __str__(self) -> str:
        return self.value


def get_class() -> Type[Album]:
    return Album
