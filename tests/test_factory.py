from app.new import sms_factory, PrimarySmsApiProvider
from app.new.providers import BaseSmsProvider


class TestSmsFactory:
    """Test SMS Factory"""

    def test_primary_factory(self):
        """Test SMS factory function - primary class"""
        klass = sms_factory("primary")
        assert isinstance(klass, PrimarySmsApiProvider)
        assert isinstance(klass, BaseSmsProvider)
