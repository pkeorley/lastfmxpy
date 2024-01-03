# Copyright © 2023 pkeorley
#
# This source code is licensed under the MIT license found in the LICENSE
# file in the root directory of this source tree.

from typing import Literal

Autocorrect = Literal[0, 1]
Extended = Literal[0, 1]

TaggingType = Literal[
    "artist",
    "album",
    "track"
]

Period = Literal[
    "overall",
    "7day",
    "1month",
    "3month",
    "6month",
    "12month"
]