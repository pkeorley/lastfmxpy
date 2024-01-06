# Copyright © 2023 pkeorley
#
# This source code is licensed under the MIT license found in the LICENSE
# file in the root directory of this source tree.

from lastfmxpy.methods.album import Album
from lastfmxpy.methods.artist import Artist
from lastfmxpy.methods.auth import Auth
from lastfmxpy.methods.chart import Chart
from lastfmxpy.methods.geo import Geo
from lastfmxpy.methods.library import Library
from lastfmxpy.methods.tag import Tag
from lastfmxpy.methods.track import Track
from lastfmxpy.methods.user import User

__all__ = [
    "Album",
    "Artist",
    "Auth",
    "Chart",
    "Geo",
    "Library",
    "Tag",
    "Track",
    "User"
]
