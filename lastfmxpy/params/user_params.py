# Copyright © 2023 pkeorley
#
# This source code is licensed under the MIT license found in the LICENSE
# file in the root directory of this source tree.

from lastfmxpy.params.base_classes import BaseUserParams
from lastfmxpy.typings import (
    TaggingType,
    Extended,
    Period
)
from lastfmxpy.utils import Utils


class GetFriends(BaseUserParams):
    def __init__(
            self,
            user: str,
            recent_tracks: str = None,
            limit: str | int = None,
            page: str | int = None,
            api_key: str = None
    ):
        """
        Get a list of the user's friends on Last.fm.
        :param user: The last.fm username to fetch the friends of.
        :param recent_tracks: Whether or not to include information about friends' recent listening in the response.
        :param limit: The number of results to fetch per page. Defaults to 50.
        :param page: The page number to fetch. Defaults to first page.
        :param api_key: A Last.fm API key.
        """
        super().__init__()

        self.user = user
        self.recent_tracks = recent_tracks
        self.limit = limit
        self.page = page
        self.api_key = api_key

    def to_json(self) -> dict:
        return Utils.remove_none_values({
            "user": self.user,
            "recenttracks": self.recent_tracks,
            "limit": self.limit,
            "page": self.page,
            "api_key": self.api_key
        })


class GetInfo(BaseUserParams):
    def __init__(
            self,
            user: str = None,
            api_key: str = None
    ):
        """
        Get information about a user profile.
        :param user: The user to fetch info for. Defaults to the authenticated user.
        :param api_key: A Last.fm API key.
        """
        super().__init__()

        self.user = user
        self.api_key = api_key

    def to_json(self) -> dict:
        return Utils.remove_none_values({
            "user": self.user,
            "api_key": self.api_key
        })


class GetLovedTracks(BaseUserParams):
    def __init__(
            self,
            user: str,
            limit: str | int = None,
            page: str | int = None,
            api_key: str = None
    ):
        """
        Get the last 50 tracks loved by a user.
        :param user: The username to fetch the loved tracks for.
        :param limit: The number of results to fetch per page. Defaults to 50.
        :param page: The page number to fetch. Defaults to first page.
        :param api_key: A Last.fm API key.
        """
        super().__init__()

        self.user = user
        self.limit = limit
        self.page = page
        self.api_key = api_key

    def to_json(self) -> dict:
        return Utils.remove_none_values({
            "user": self.user,
            "limit": self.limit,
            "page": self.page,
            "api_key": self.api_key
        })


class GetPersonalTags(BaseUserParams):
    def __init__(
            self,
            user: str,
            tag: str,
            tagging_type: TaggingType,
            limit: str | int = None,
            page: str | int = None,
            api_key: str = None
    ):
        """
        Get the user's personal tags
        :param user: The user who performed the taggings.
        :param tag: The tag you're interested in.
        :param tagging_type: The type of items which have been tagged
        :param limit: The number of results to fetch per page. Defaults to 50.
        :param page: The page number to fetch. Defaults to first page.
        :param api_key: A Last.fm API key.
        """
        super().__init__()

        self.user = user
        self.tag = tag
        self.tagging_type = tagging_type
        self.limit = limit
        self.page = page
        self.api_key = api_key

    def to_json(self) -> dict:
        return Utils.remove_none_values({
            "user": self.user,
            "tag": self.tag,
            "taggingtype": self.tagging_type,
            "limit": self.limit,
            "page": self.page,
            "api_key": self.api_key
        })


class GetRecentTracks(BaseUserParams):
    def __init__(
            self,
            user: str,
            limit: str | int = None,
            page: str | int = None,
            extended: Extended = None,
            from_: str = None,
            to: str = None,
            api_key: str = None
    ):
        """
        Get a list of the recent tracks listened to by this user. Also includes the currently playing track with the nowplaying="true" attribute if the user is currently listening.
        :param user: The last.fm username to fetch the recent tracks of.
        :param limit: The number of results to fetch per page. Defaults to 50. Maximum is 200.
        :param page: The page number to fetch. Defaults to first page.
        :param extended: Includes extended data in each artist, and whether or not the user has loved each track
        :param from_: Beginning timestamp of a range - only display scrobbles after this time, in UNIX timestamp format (integer number of seconds since 00:00:00, January 1st 1970 UTC). This must be in the UTC time zone.
        :param to: End timestamp of a range - only display scrobbles before this time, in UNIX timestamp format (integer number of seconds since 00:00:00, January 1st 1970 UTC). This must be in the UTC time zone.
        :param api_key: A Last.fm API key.
        """
        super().__init__()

        self.user = user
        self.limit = limit
        self.page = page
        self.extended = extended
        self.from_ = from_
        self.to = to
        self.api_key = api_key

    def to_json(self) -> dict:
        return Utils.remove_none_values({
            "user": self.user,
            "limit": self.limit,
            "page": self.page,
            "extended": self.extended,
            "from": self.from_,
            "to": self.to,
            "api_key": self.api_key
        })


class GetTopAlbums(BaseUserParams):
    def __init__(
            self,
            user: str,
            period: Period = None,
            limit: str | int = None,
            page: str | int = None,
            api_key: str = None
    ):
        """
        Get the top albums listened to by a user. You can stipulate a time period. Sends the overall chart by default.
        :param user: The username to fetch top albums for.
        :param period: overall | 7day | 1month | 3month | 6month | 12month - The time period over which to retrieve top albums for.
        :param limit: The number of results to fetch per page. Defaults to 50.
        :param page: The page number to fetch. Defaults to first page.
        :param api_key: A Last.fm API key.
        """
        super().__init__()

        self.user = user
        self.period = period
        self.limit = limit
        self.page = page
        self.api_key = api_key

    def to_json(self) -> dict:
        return Utils.remove_none_values({
            "user": self.user,
            "period": self.period,
            "limit": self.limit,
            "page": self.page,
            "api_key": self.api_key
        })


class GetTopArtists(BaseUserParams):
    def __init__(
            self,
            user: str,
            period: Period = None,
            limit: str | int = None,
            page: str | int = None,
            api_key: str = None
    ):
        """
        Get the top artists listened to by a user. You can stipulate a time period. Sends the overall chart by default.
        :param user: The username to fetch top artists for.
        :param period: overall | 7day | 1month | 3month | 6month | 12month - The time period over which to retrieve top artists for.
        :param limit: The number of results to fetch per page. Defaults to 50.
        :param page: The page number to fetch. Defaults to first page.
        :param api_key: A Last.fm API key.
        """
        super().__init__()

        self.user = user
        self.period = period
        self.limit = limit
        self.page = page
        self.api_key = api_key

    def to_json(self) -> dict:
        return Utils.remove_none_values({
            "user": self.user,
            "period": self.period,
            "limit": self.limit,
            "page": self.page,
            "api_key": self.api_key
        })


class GetTopTags(BaseUserParams):
    def __init__(
            self,
            user: str,
            limit: str | int = None,
            api_key: str | None = None
    ):
        """
        Get the top tags used by this user.
        :param user: The username
        :param limit: Limit the number of tags returned
        :param api_key: A Last.fm API key.
        """
        super().__init__()

        self.user = user
        self.limit = limit
        self.api_key = api_key

    def to_json(self) -> dict:
        return Utils.remove_none_values({
            "user": self.user,
            "limit": self.limit,
            "api_key": self.api_key
        })


class GetTopTracks(BaseUserParams):
    def __init__(
            self,
            user: str,
            period: Period = None,
            limit: str | int = None,
            page: str | int = None,
            api_key: str = None
    ):
        """
        Get the top tracks listened to by a user. You can stipulate a time period. Sends the overall chart by default.
        :param user: The username to fetch top tracks for.
        :param period: overall | 7day | 1month | 3month | 6month | 12month - The time period over which to retrieve top tracks for.
        :param limit: The number of results to fetch per page. Defaults to 50.
        :param page: The page number to fetch. Defaults to first page.
        :param api_key: A Last.fm API key.
        """
        super().__init__()

        self.user = user
        self.period = period
        self.limit = limit
        self.page = page
        self.api_key = api_key

    def to_json(self) -> dict:
        return Utils.remove_none_values({
            "user": self.user,
            "period": self.period,
            "limit": self.limit,
            "page": self.page,
            "api_key": self.api_key
        })


class GetWeeklyAlbumChart(BaseUserParams):
    def __init__(
            self,
            user: str,
            from_: str = None,
            to: str = None,
            api_key: str = None
    ):
        """
        Get an album chart for a user profile, for a given date range. If no date range is supplied, it will return the most recent album chart for this user.
        :param user: The last.fm username to fetch the charts of.
        :param from_: The date at which the chart should start from. See GetChartsList() for more.
        :param to:  The date at which the chart should end on. See GetChartsList() for more.
        :param api_key: A Last.fm API key.
        """
        super().__init__()

        self.user = user
        self.from_ = from_
        self.to = to
        self.api_key = api_key

    def to_json(self) -> dict:
        return Utils.remove_none_values({
            "user": self.user,
            "from": self.from_,
            "to": self.to,
            "api_key": self.api_key
        })


class GetWeeklyArtistChart(BaseUserParams):
    def __init__(
            self,
            user: str,
            from_: str = None,
            to: str = None,
            api_key: str = None
    ):
        """
        Get an artist chart for a user profile, for a given date range. If no date range is supplied, it will return the most recent artist chart for this user.
        :param user: The last.fm username to fetch the charts of.
        :param from_: The date at which the chart should start from. See GetWeeklyChartList() for more.
        :param to:  The date at which the chart should end on. See GetWeeklyChartList() for more.
        :param api_key: A Last.fm API key.
        """
        super().__init__()

        self.user = user
        self.from_ = from_
        self.to = to
        self.api_key = api_key

    def to_json(self) -> dict:
        return Utils.remove_none_values({
            "user": self.user,
            "from": self.from_,
            "to": self.to,
            "api_key": self.api_key
        })


class GetWeeklyChartList(BaseUserParams):
    def __init__(
            self,
            user: str,
            api_key: str = None
    ):
        """
        Get a list of available charts for this user, expressed as date ranges which can be sent to the chart services.
        :param user: The last.fm username to fetch the charts list for.
        :param api_key: A Last.fm API key.
        """
        super().__init__()

        self.user = user
        self.api_key = api_key

    def to_json(self) -> dict:
        return Utils.remove_none_values({
            "user": self.user,
            "api_key": self.api_key
        })


class GetWeeklyTrackChart(BaseUserParams):
    def __init__(
            self,
            user: str,
            from_: str = None,
            to: str = None,
            api_key: str = None
    ):
        """
        Get a track chart for a user profile, for a given date range. If no date range is supplied, it will return the most recent track chart for this user.
        :param user: The last.fm username to fetch the charts of.
        :param from_: The date at which the chart should start from. See GetWeeklyChartList() for more.
        :param to:  The date at which the chart should end on. See GetWeeklyChartList() for more.
        :param api_key: A Last.fm API key.
        """
        super().__init__()

        self.user = user
        self.from_ = from_
        self.to = to
        self.api_key = api_key

    def to_json(self) -> dict:
        return Utils.remove_none_values({
            "user": self.user,
            "from": self.from_,
            "to": self.to,
            "api_key": self.api_key
        })
