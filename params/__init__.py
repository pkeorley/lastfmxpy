# Copyright © 2023 pkeorley
#
# This source code is licensed under the MIT license found in the LICENSE
# file in the root directory of this source tree.

from .album_params import (
    AddTags as AlbumAddTags,
    GetInfo as AlbumGetInfo,
    GetTags as AlbumGetTags,
    GetTopTags as AlbumGetTopTags,
    RemoveTag as AlbumRemoveTag,
    Search as AlbumSearch
)
from .artist_params import (
    AddTags as ArtistAddTags,
    GetCorrection as ArtistGetCorrection,
    GetInfo as ArtistGetInfo,
    GetSimilar as ArtistGetSimilar,
    GetTags as ArtistGetTags,
    GetTopAlbums as ArtistGetTopAlbums,
    GetTopTags as ArtistGetTopTags,
    GetTopTracks as ArtistGetTopTracks,
    RemoveTag as ArtistRemoveTag,
    Search as ArtistSearch
)
from .auth_params import (
    GetMobileSession as AuthGetMobileSession,  # deprecated as last.fm
    GetSession as AuthGetSession,
    GetToken as AuthGetToken
)
from .chart_params import (
    GetTopArtists as ChartGetTopArtists,
    GetTopTags as ChartGetTopTags,
    GetTopTracks as ChartGetTopTracks
)
from .geo_params import (
    GetTopArtists as GeoGetTopArtists,
    GetTopTracks as GeoGetTopTracks
)
from .library_params import (
    GetArtists as LibraryGetArtists
)
from .tag_params import (
    GetInfo as TagGetInfo,
    GetSimilar as TagGetSimilar,
    GetTopAlbums as TagGetTopAlbums,
    GetTopArtists as TagGetTopArtists,
    GetTopTracks as TagGetTopTracks,
    GetWeeklyChartList as TagGetWeeklyChartList
)
from .track_params import (
    AddTags as TrackAddTags,
    GetCorrection as TrackGetCorrection,
    GetInfo as TrackGetInfo,
    GetSimilar as TrackGetSimilar,
    GetTags as TrackGetTags,
    GetTopTags as TrackGetTopTags,
    Love as TrackLove,
    RemoveTag as TrackRemoveTag,
    Scrobble as TrackScrobble,
    Search as TrackSearch,
    Unlove as TrackUnlove,
    UpdateNowPlaying as TrackUpdateNowPlaying
)
from .user_params import (
    GetFriends as UserGetFriends,
    GetInfo as UserGetInfo,
    GetLovedTracks as UserGetLovedTracks,
    GetPersonalTags as UserGetPersonalTags,
    GetRecentTracks as UserGetRecentTracks,
    GetTopAlbums as UserGetTopAlbums,
    GetTopArtists as UserGetTopArtists,
    GetTopTags as UserGetTopTags,
    GetTopTracks as UserGetTopTracks,
    GetWeeklyAlbumChart as UserGetWeeklyAlbumChart,
    GetWeeklyArtistChart as UserGetWeeklyArtistChart,
    GetWeeklyChartList as UserGetWeeklyChartList,
    GetWeeklyTrackChart as UserGetWeeklyTrackChart
)

__all__ = [
    "AlbumAddTags",
    "AlbumGetInfo",
    "AlbumGetTags",
    "AlbumGetTopTags",
    "AlbumRemoveTag",
    "AlbumSearch",
    "ArtistAddTags",
    "ArtistGetCorrection",
    "ArtistGetInfo",
    "ArtistGetSimilar",
    "ArtistGetTags",
    "ArtistGetTopAlbums",
    "ArtistGetTopTags",
    "ArtistGetTopTracks",
    "ArtistRemoveTag",
    "ArtistSearch",
    "AuthGetSession",
    "AuthGetToken",
    "ChartGetTopArtists",
    "ChartGetTopTags",
    "ChartGetTopTracks",
    "GeoGetTopArtists",
    "GeoGetTopTracks",
    "LibraryGetArtists",
    "TagGetInfo",
    "TagGetSimilar",
    "TagGetTopAlbums",
    "TagGetTopArtists",
    "TagGetTopTracks",
    "TagGetWeeklyChartList",
    "TrackAddTags",
    "TrackGetCorrection",
    "TrackGetInfo",
    "TrackGetSimilar",
    "TrackGetTags",
    "TrackGetTopTags",
    "TrackLove",
    "TrackRemoveTag",
    "TrackScrobble",
    "TrackSearch",
    "TrackUnlove",
    "TrackUpdateNowPlaying",
    "UserGetFriends",
    "UserGetInfo",
    "UserGetLovedTracks",
    "UserGetPersonalTags",
    "UserGetRecentTracks",
    "UserGetTopAlbums",
    "UserGetTopArtists",
    "UserGetTopTags",
    "UserGetTopTracks",
    "UserGetWeeklyAlbumChart",
    "UserGetWeeklyArtistChart",
    "UserGetWeeklyChartList",
    "UserGetWeeklyTrackChart",
]
