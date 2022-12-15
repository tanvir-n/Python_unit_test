from app.new import sms_factory, PrimarySmsApiProvider, SecondarySmsApiProvider
from app.new.providers import BaseSmsProvider


class TestSmsFactory:
    """Test SMS Factory"""

    def test_sms_factory(self):
        """Test SMS factory function - primary and secondary class"""
        primary_obj = sms_factory("primary")
        secendary_obj = sms_factory('secondary')
        assert isinstance(primary_obj, PrimarySmsApiProvider)
        assert isinstance(secendary_obj, SecondarySmsApiProvider)
        assert isinstance(primary_obj, BaseSmsProvider)
