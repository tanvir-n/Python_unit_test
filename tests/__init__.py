import uuid
from unittest import mock


class BaseSmsTestCases:
    """Base test class"""

    _cleanups = []
    uuid_patcher = None
    FAKE_UUID = "FAKE_UUID"
    CORRECT_CONTENT = "content"
    CORRECT_PHONE = "123456789"
    CORRECT_COUNTRY = "PL"

    @classmethod
    def setup_class(cls):
        """setUpClass method"""
        cls.uuid_patcher = mock.patch.object(uuid, "uuid4", return_value=cls.FAKE_UUID)
        cls.argv_mock = cls.uuid_patcher.start()

    @classmethod
    def teardown_class(cls):
        cls.uuid_patcher.stop()
