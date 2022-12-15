import pytest
from unittest import mock

from app import errors
from app.old import sms_primary_api, sms_secondary_api
from . import BaseSmsTestCases


class TestSmsFunctions(BaseSmsTestCases):
    """Test SMS API functions style"""

    def test_primary_api_success(self):
        """Test Primary API - success"""
        status, response = sms_primary_api(
            self.CORRECT_CONTENT, self.CORRECT_PHONE, self.CORRECT_COUNTRY
        )
        assert status
        assert response == {"recipient": "0048123456789", "status": "SENT", "api": "1"}

    @mock.patch(
        "app.old.fake_primary_external_api",
        mock.MagicMock(return_value={"api": "1", "status": "ERROR"}),
    )
    def test_primary_api_fail(self):
        """Test Primary API - fail"""
        status, response = sms_primary_api(
            self.CORRECT_CONTENT, self.CORRECT_PHONE, self.CORRECT_COUNTRY
        )
        assert not status
        assert response == {"api": "1", "status": "ERROR"}

    def test_primary_api_wrong_phone(self):
        """Test Primary API - wrong phone exception"""
        with pytest.raises(errors.InvalidPhoneNumber):
            sms_primary_api("test content", "0800CALLUS")

    def test_secondary_api_success(self):
        """Test Secondary API - success"""
        status, response = sms_secondary_api(self.CORRECT_CONTENT, self.CORRECT_PHONE)
        assert status
        assert response == {"status": "OK", "api": "2", "id": self.FAKE_UUID}
