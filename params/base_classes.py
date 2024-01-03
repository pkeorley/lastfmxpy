# Copyright © 2023 pkeorley
#
# This source code is licensed under the MIT license found in the LICENSE
# file in the root directory of this source tree.

class BaseParams:
    def __init__(self):
        pass

    def to_json(self) -> dict:
        raise NotImplementedError("to_json() is not implemented")


class BaseAlbumParams(BaseParams):
    def __init__(self):
        super().__init__()


class BaseArtistParams(BaseParams):
    def __init__(self):
        super().__init__()


class BaseAuthParams(BaseParams):
    def __init__(self):
        super().__init__()


class BaseChartParams(BaseParams):
    def __init__(self):
        super().__init__()


class BaseGeoParams(BaseParams):
    def __init__(self):
        super().__init__()


class BaseLibraryParams(BaseParams):
    def __init__(self):
        super().__init__()


class BaseTagParams(BaseParams):
    def __init__(self):
        super().__init__()


class BaseTrackParams(BaseParams):
    def __init__(self):
        super().__init__()


class BaseUserParams(BaseParams):
    def __init__(self):
        super().__init__()
