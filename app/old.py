from . import errors
from . import settings
from .fake import fake_primary_external_api, fake_secondary_external_api


def sms_primary_api(content, phone, country_code="PL"):
    """Old Primary SMS API provider"""
    if country_code and country_code not in settings.COUNTRY_CODES.keys():
        raise errors.InvalidCountryException("Invalid country code")
    if not phone.isdigit():
        raise errors.InvalidPhoneNumber("Invalid phone number")
    if len(content) > 70:
        raise errors.InvalidContentLength("Invalid content length")

    msg = {
        "content": content,
        "phone": settings.COUNTRY_CODES[country_code] + phone,
        "sender": "Alice",
        "api_key": settings.PRIMARY_API_KEY,
    }

    response = fake_primary_external_api(msg)

    if response.get("status") == "SENT":
        return True, response
    return False, response


def sms_secondary_api(content, phone, country_code="PL"):
    """Old Secondary SMS API provider"""
    if country_code and country_code not in settings.COUNTRY_CODES.keys():
        raise errors.InvalidCountryException("Invalid country code")
    if not phone.isdigit():
        raise errors.InvalidPhoneNumber("Invalid phone number")
    if len(content) > 160:
        raise errors.InvalidContentLength("Invalid content length")

    msg = {
        "body": content,
        "recipient": settings.COUNTRY_CODES[country_code] + phone,
        "sender_name": "Alice",
        "auth_key": settings.SECONDARY_API_KEY,
    }

    response = fake_secondary_external_api(msg)

    return response.get("status") == "OK", response
