# Copyright © 2023 pkeorley
#
# This source code is licensed under the MIT license found in the LICENSE
# file in the root directory of this source tree.

from enum import Enum
from typing import Type


class Auth(Enum):
    GET_MOBILE_SESSION: str = "auth.getMobileSession"
    GET_SESSION: str = "auth.getSession"
    GET_TOKEN: str = "auth.getToken"

    def __str__(self) -> str:
        return self.value


def get_class() -> Type[Auth]:
    return Auth
