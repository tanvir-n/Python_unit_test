from app import settings
from .base import BaseSmsProvider

from app import errors
from app.fake import fake_secondary_external_api


class SecondarySmsApiProvider(BaseSmsProvider):
    """
    Secondary SMS API Provide
    Write this class from scratch based on `primary.py` and `old.py` files
    """

    #
    # @TODO: Implement it
    #
    API_KEY = settings.SECONDARY_API_KEY

    def _validate_set_recipient(self, *args):
        """Validate recipient using the same logic as defined in `old.py` file.
        Throw appropriate exception or return a boolean"""
        #
        # @TODO: Implement it
        #
        if args[0] and not args[0].isdigit():
            raise errors.InvalidPhoneNumber("Invalid phone number")
        if len(args) > 1 and args[1] not in settings.COUNTRY_CODES.keys():
            raise errors.InvalidCountryException("Invalid country code")
        return True

    def _validate_set_content(self, *args):
        """Validate content.
        Throw appropriate exception or return a boolean"""
        #
        # @TODO: Implement it
        #
        if len(args[0]) > 160:
            raise errors.InvalidContentLength("Invalid content length")
        return True

    def _validate_before_sending(self):
        """Check if content and recipient are set.
        Throw appropriate exception from `app.errors` module"""
        #
        # @TODO: Implement it
        #
        if self.recipient is None:
            raise errors.RecipientNotSet('Recipient not set')
        if self.content is None:
            raise errors.ContentNotSet('Content not set')

    def _process_response(self, resp):
        """Check response content.
        Return (boolean, resp)"""
        #
        # @TODO: Implement it
        #
        return resp.get("status") == "OK", resp

    def _prepare_payload(self):
        """Construct and return payload - check `old.py` for the implementation details"""
        #
        # @TODO: Implement it
        #
        payload = {}        
        payload.update({
            'body': self.content,
            'recipient': self.recipient,
            "sender_name": "Alice",
            "auth_key": self.API_KEY,
        })

        return payload
    
    def send(self):
        """Send the message"""
        self._validate_before_sending()
        payload = self._prepare_payload()
        response = fake_secondary_external_api(payload)
        return self._process_response(response)
