
from enum import Enum


class AuthorizationPlatformType(str, Enum):
    DEFAULT = 'DEFAULT'
    OAUTH = 'OAUTH'
    CUSTOM = 'CUSTOM'