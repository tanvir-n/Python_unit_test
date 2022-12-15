class BaseError(Exception):
    """Base exception class"""


class InvalidCountryException(BaseError):
    """Invalid country exception"""


class InvalidPhoneNumber(BaseError):
    """Invalid phone number"""


class InvalidContentLength(BaseError):
    """Invalid content length exception"""


class ContentNotSet(BaseError):
    """Content not set exception"""


class RecipientNotSet(BaseError):
    """Recipient not set exception"""
