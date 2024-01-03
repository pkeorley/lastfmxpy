# Copyright © 2023 pkeorley
#
# This source code is licensed under the MIT license found in the LICENSE
# file in the root directory of this source tree.

from enum import Enum


class LFPError(Exception):
    def __init__(self, *args: object):
        Exception.__init__(self, args)


class LFPWarning(Warning, LFPError):
    def __init__(self, *args: object):
        Warning.__init__(self, args)


class LFPPanic(LFPError):
    def __init__(self, *args: object):
        LFPError.__init__(self, args)


class Errors(Enum):
    INVALID_SERVICE: int = 2
    INVALID_METHOD: int = 3
    AUTHENTICATION_FAILED: int = 4
    INVALID_FORMAT: int = 5
    INVALID_PARAMETERS: int = 6
    INVALID_RESOURCE_SPECIFIED: int = 7
    OPERATION_FAILED: int = 8
    INVALID_SESSION_KEY: int = 9
    INVALID_API_KEY: int = 10
    SERVICE_OFFLINE: int = 11
    INVALID_METHOD_SIGNATURE_SUPPLIED: int = 13
    THERE_WAS_A_TEMPORARY_ERROR_PROCESSING_YOUR_REQUEST: int = 16
    SUSPENDED_API_KEY: int = 26
    RATE_LIMIT_EXCEEDED: int = 29

    def __int__(self) -> int:
        return self.value

    def __str__(self):
        return self.name
