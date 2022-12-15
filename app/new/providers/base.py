import abc
from functools import wraps

from app import settings


class BaseSmsProvider(metaclass=abc.ABCMeta):
    """Base SMS Provider class"""

    recipient, content = None, None
    SENDER_NAME = "Alice"
    COUNTRY_CODES = settings.COUNTRY_CODES

    # pylint: disable=no-self-argument
    def _validation(func):
        """Validation decorator"""

        @wraps(func)
        def wrapped(obj, *args, **kwargs):
            # pylint: disable=no-member, not-callable
            getattr(obj, "_validate_" + func.__name__)(*args)
            return func(obj, *args, **kwargs)

        return wrapped

    @abc.abstractmethod
    def send(self):
        """Abstract sending method"""
        pass

    @abc.abstractmethod
    def _process_response(self, resp):
        """Protected abstract method responsible for response processing"""
        pass

    @abc.abstractmethod
    def _prepare_payload(self):
        """Protected abstract method responsible for creating payload"""
        pass

    @_validation
    def set_content(self, content):
        """Set content and make the method chainable"""
        #
        # @TODO: Implement it
        #
        self.content = content
        return self
        

    @_validation
    def set_recipient(self, phone_number, country_code="PL"):
        """Set recipient attribute - remember to add a country code like in the `old.py` file.
        Make the method chainable"""
        #
        # @TODO: Implement it
        #
        # if country_code and country_code not in self.COUNTRY_CODES.keys():
        #     raise errors.InvalidCountryException("Invalid country code")
        # if not phone_number.isdigit():
        #     raise errors.InvalidPhoneNumber("Invalid phone number")
        
        self.recipient = self.COUNTRY_CODES[country_code] + phone_number
        return self