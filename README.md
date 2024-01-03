# Last FM API (lastfmxpy)

![Static Badge](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![GitHub License](https://img.shields.io/github/license/pkeorley/telegram-tui)
![GitHub issues](https://img.shields.io/github/issues/pkeorley/telegram-tui)
![GitHub commit activity (branch)](https://img.shields.io/github/commit-activity/y/pkeorley/lastfmxpy)
![GitHub contributors](https://img.shields.io/github/contributors/pkeorley/lastfmxpy)

-----

* **lastfmxpy** *(Last FM Api)* - is a mono-repository that has a user-friendly interface for interacting with the largest music service [last.fm](https://www.last.fm). This library implements all the standard methods available on [this page](https://www.last.fm/api).

**Table of contents**
- [Project goals](#project-goals)
- [Documentation](#documentation)
- [Implemented functionalities](#implemented-functionalities)
- - [The ./methods directory](#the-methods-directory)
- - [The ./params directory](#the-params-directory)
- [Licence](#license)

## Project goals
- [x] Implement all existing methods in the [Last FM API Docs](https://www.last.fm/api)
- [x] Provide a convenient interface for sending requests to the server
- [x] Add doc-strings to each method or class
- [ ] Add support for documentation in different languages
- [ ] Add asynchronous support

## Documentation

**Installation**: To install this library, you need to enter the following command
```shell
pip install -U lastfmxpy
```
**Usage**: 

```python
import json

from lastfm_api import (
    api,
    methods,
    params,
)

# Initialise our object through which we will interact with last.fm
api = api.LastFMApi(
    api_key="...", # Get here https://www.last.fm/api/account/create,
    shared_secret="..." # Also get here （￣︶￣）↗　
)

# Get all information about the artist in JSON as a string 
response: str = api.post(
    
    # Specify which method we will use
    method=methods.User.GET_INFO,
    
    # Let us specify our parameters
    params=params.UserGetInfo(
        user="pkeorley"
    ),
    
    # We can also specify additional parameters
    additional_params=dict(format="json")

)

# Let's show our data in a convenient form on the screen
data: str = json.dumps(
    json.loads(response),
    indent=4,
    ensure_ascii=False
)

print(data)
```

**All available methods ([./methods/\_\_init\_\_.py](/methods/__init__.py))**
```python
from lastfm_api.methods import (
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
```

**All available parameters ([./params/\_\_init\_\_.py](/params/__init__.py)):**

```python
from lastfm_api.params import (
    AlbumAddTags,
    AlbumGetInfo,
    AlbumGetTags,
    AlbumGetTopTags,
    AlbumRemoveTag,
    AlbumSearch
)

from lastfm_api.params import (
    AlbumAddTags,
    AlbumGetInfo,
    AlbumGetTags,
    AlbumGetTopTags,
    AlbumRemoveTag,
    AlbumSearch
)
from lastfm_api.params import (
    ArtistAddTags,
    ArtistGetCorrection,
    ArtistGetInfo,
    ArtistGetSimilar,
    ArtistGetTags,
    ArtistGetTopAlbums,
    ArtistGetTopTags,
    ArtistGetTopTracks,
    ArtistRemoveTag,
    ArtistSearch
)
from lastfm_api.params import (
    AuthGetMobileSession,  # deprecated as last.fm
    AuthGetSession,
    AuthGetToken
)
from lastfm_api.params import (
    ChartGetTopArtists,
    ChartGetTopTags,
    ChartGetTopTracks
)
from lastfm_api.params import (
    GeoGetTopArtists,
    GeoGetTopTracks
)
from lastfm_api.params import (
    LibraryGetArtists
)
from lastfm_api.params import (
    TagGetInfo,
    TagGetSimilar,
    TagGetTopAlbums,
    TagGetTopArtists,
    TagGetTopTracks,
    TagGetWeeklyChartList
)
from lastfm_api.params import (
    TrackAddTags,
    TrackGetCorrection,
    TrackGetInfo,
    TrackGetSimilar,
    TrackGetTags,
    TrackGetTopTags,
    TrackLove,
    TrackRemoveTag,
    TrackScrobble,
    TrackSearch,
    TrackUnlove,
    TrackUpdateNowPlaying
)
from lastfm_api.params import (
    UserGetFriends,
    UserGetInfo,
    UserGetLovedTracks,
    UserGetPersonalTags,
    UserGetRecentTracks,
    UserGetTopAlbums,
    UserGetTopArtists,
    UserGetTopTags,
    UserGetTopTracks,
    UserGetWeeklyAlbumChart,
    UserGetWeeklyArtistChart,
    UserGetWeeklyChartList,
    UserGetWeeklyTrackChart
)
```

## License

`lastfmxpy` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.