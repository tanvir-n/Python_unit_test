import abc
from functools import wraps

from app import settings


class BaseSmsProvider(metaclass=abc.ABCMeta):

    recipient, content = None, None
    SENDER_NAME = "Alice"
    COUNTRY_CODES = settings.COUNTRY_CODES

    def _validation(func):

        @wraps(func)
        def wrapped(obj, *args, **kwargs):
            getattr(obj, "_validate_" + func.__name__)(*args)
            return func(obj, *args, **kwargs)

        return wrapped

    @abc.abstractmethod
    def send(self):
        pass

    @abc.abstractmethod
    def _process_response(self, resp):
        pass

    @abc.abstractmethod
    def _prepare_payload(self):
        pass

    @_validation
    def set_content(self, content):
        self.content = content
        return self
        

    @_validation
    def set_recipient(self, phone_number, country_code="PL"):    
        self.recipient = self.COUNTRY_CODES[country_code] + phone_number
        return self