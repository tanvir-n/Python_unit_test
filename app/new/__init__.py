"""New SMS module"""
from .providers import PrimarySmsApiProvider, SecondarySmsApiProvider


def sms_factory(api):
    """Implement a factory that creates appropriate objects based on the `api` argument.
    When `api` is unknown, throw NotImplementedError exception."""
    #
    # @TODO: Implement it
    #
    if api:
        if api == 'primary':
            return PrimarySmsApiProvider()
        elif api == 'secondary':
            return SecondarySmsApiProvider()
            
    return NotImplementedError()

