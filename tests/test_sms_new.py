import pytest

from app import errors
from app.new import sms_factory, PrimarySmsApiProvider
from app.old import sms_primary_api, sms_secondary_api
from . import BaseSmsTestCases


class TestSmsPrimaryClasses(BaseSmsTestCases):

    @pytest.fixture
    def sender(self):
        """Sender fixture"""
        return sms_factory("primary")

    def test_api_response(self, sender):
        status, response = (
            sender.set_recipient(self.CORRECT_PHONE)
            .set_content(self.CORRECT_CONTENT)
            .send()
        )
        assert status
        assert response == {"recipient": "0048123456789", "status": "SENT", "api": "1"}

    def test_recipient_not_set(self, sender):
        with pytest.raises(errors.RecipientNotSet):
            sender.set_content(self.CORRECT_CONTENT).send()

    def test_compare_old_and_new(self, sender):
        assert (
            sms_primary_api(
                self.CORRECT_CONTENT, self.CORRECT_PHONE, self.CORRECT_COUNTRY
            )
            == sender.set_recipient(self.CORRECT_PHONE)
            .set_content(self.CORRECT_CONTENT)
            .send()
        )

    def test_api_wrong_auth_key(self, sender):
        sender.API_KEY = "wrong api key"
        status, response = (
            sender.set_recipient(self.CORRECT_PHONE)
            .set_content(self.CORRECT_CONTENT)
            .send()
        )
        assert not status
        assert response == {"api": "1", "status": "403"}

    def test_process_response_method_ok(self):
        response = {"status": "SENT"}
        # pylint: disable=protected-access
        assert PrimarySmsApiProvider()._process_response(response) == (True, response)


class TestSmsSecondaryClasses(BaseSmsTestCases):

    @pytest.fixture
    def sender(self):
        """Sender fixture"""
        return sms_factory("secondary")

    def test_api_response(self, sender):
        status, response = (
            sender.set_recipient(self.CORRECT_PHONE)
            .set_content(self.CORRECT_CONTENT)
            .send()
        )
        assert status
        assert response == {"status": "OK", "id": self.FAKE_UUID, "api": "2"}

    def test_recipient_not_set(self, sender):
        with pytest.raises(errors.RecipientNotSet):
            sender.set_content(self.CORRECT_CONTENT).send()

    def test_compare_old_and_new(self, sender):
        assert (
            sms_secondary_api(
                self.CORRECT_CONTENT, self.CORRECT_PHONE, self.CORRECT_COUNTRY
            )
            == sender.set_recipient(self.CORRECT_PHONE)
            .set_content(self.CORRECT_CONTENT)
            .send()
        )
