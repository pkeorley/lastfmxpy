from typing import Union

from lastfmxpy.methods import (
    Album,
    Artist,
    Auth,
    Chart,
    Geo,
    Library,
    Tag,
    Track,
    User
)
from lastfmxpy.params.base_classes import (
    BaseAlbumParams,
    BaseArtistParams,
    BaseAuthParams,
    BaseChartParams,
    BaseGeoParams,
    BaseLibraryParams,
    BaseTagParams,
    BaseTrackParams,
    BaseUserParams
)

PostMethod = Union[
    Album,
    Artist,
    Auth,
    Chart,
    Geo,
    Library,
    Tag,
    Track,
    User
]

PostParam = Union[
    BaseAlbumParams,
    BaseArtistParams,
    BaseAuthParams,
    BaseChartParams,
    BaseGeoParams,
    BaseLibraryParams,
    BaseTagParams,
    BaseTrackParams,
    BaseUserParams
]