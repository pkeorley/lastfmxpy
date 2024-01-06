# Copyright © 2023 pkeorley
#
# This source code is licensed under the MIT license found in the LICENSE
# file in the root directory of this source tree.

from lastfmxpy.params.base_classes import BaseAuthParams
from lastfmxpy.utils import Utils


class GetMobileSession(BaseAuthParams):
    def __init__(
            self,
            username: str,
            password: str,
            api_key: str = None,
            api_sig: str = None
    ):
        """
        **DEPRECATED BEHAVIOUR**
        *This method has other parameters which are now deprecated and should not be used.*

        Create a web service session for a user. Used for authenticating a user when the password can be inputted by the user. Accepts email address as well, so please use the username supplied in the output. Only suitable for standalone mobile devices. See the authentication how-to for more. You must use HTTPS and POST in order to use this method.

        :param username: The last.fm username or email address.
        :param password: The password in plain text.
        :param api_key: A Last.fm API key.
        :param api_sig: A Last.fm method signature. See authentication (https://www.last.fm/api/authentication) for more information.
        """
        super().__init__()

        self.username = username
        self.password = password
        self.api_key = api_key
        self.api_sig = api_sig

    def to_json(self) -> dict:
        return Utils.remove_none_values({
            "username": self.username,
            "password": self.password,
            "api_key": self.api_key,
            "api_sig": self.api_sig
        })


class GetSession(BaseAuthParams):
    def __init__(
            self,
            token: str,
            api_key: str = None,
            api_sig: str = None
    ):
        """
        Fetch a session key for a user. The third step in the authentication process. See the authentication how-to for more information.
        :param token: A 32-character ASCII hexadecimal MD5 hash returned by step 1 of the authentication process (following the granting of permissions to the application by the user)
        :param api_key:A Last.fm API key.
        :param api_sig: A Last.fm method signature. See authentication (https://www.last.fm/api/authentication) for more information.
        """
        super().__init__()

        self.token = token
        self.api_key = api_key
        self.api_sig = api_sig

    def to_json(self) -> dict:
        return Utils.remove_none_values({
            "token": self.token,
            "api_key": self.api_key,
            "api_sig": self.api_sig
        })


class GetToken(BaseAuthParams):
    def __init__(
            self,
            api_key: str,
            api_sig: str = None
    ):
        """
        Fetch an unathorized request token for an API account. This is step 2 of the authentication process for desktop applications. Web applications do not need to use this service.
        :param api_key: A Last.fm API key.
        :param api_sig: A Last.fm method signature. See authentication (https://www.last.fm/api/authentication) for more information.
        """
        super().__init__()

        self.api_key = api_key
        self.api_sig = api_sig

    def to_json(self) -> dict:
        return Utils.remove_none_values({
            "api_key": self.api_key,
            "api_sig": self.api_sig
        })
