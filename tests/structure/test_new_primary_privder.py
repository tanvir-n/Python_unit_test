import base64
import unittest

import app.new.providers.primary


class StructureTestSuite(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.MODULE = app.new.providers.primary

    def test_class_exists_primarysmsapiprovider(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"UHJpbWFyeVNtc0FwaVByb3ZpZGVy").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'UHJpbWFyeVNtc0FwaVByb3ZpZGVy').decode()}` "
            f"is not found, but it was marked as required.",
        )

    def test_class_function_exists_primarysmsapiprovider__prepare_payload(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"UHJpbWFyeVNtc0FwaVByb3ZpZGVy").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'UHJpbWFyeVNtc0FwaVByb3ZpZGVy').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"UHJpbWFyeVNtc0FwaVByb3ZpZGVy").decode()
        )
        self.assertIn(
            base64.b64decode(
                b"UHJpbWFyeVNtc0FwaVByb3ZpZGVyLl9wcmVwYXJlX3BheWxvYWQ="
            ).decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'UHJpbWFyeVNtc0FwaVByb3ZpZGVyLl9wcmVwYXJlX3BheWxvYWQ=').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'UHJpbWFyeVNtc0FwaVByb3ZpZGVy').decode()}`, "
            f"but it was marked as required.",
        )

    def test_class_function_signature_match_primarysmsapiprovider__prepare_payload(
        self,
    ):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"UHJpbWFyeVNtc0FwaVByb3ZpZGVy").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'UHJpbWFyeVNtc0FwaVByb3ZpZGVy').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"UHJpbWFyeVNtc0FwaVByb3ZpZGVy").decode()
        )
        self.assertIn(
            base64.b64decode(
                b"UHJpbWFyeVNtc0FwaVByb3ZpZGVyLl9wcmVwYXJlX3BheWxvYWQ="
            ).decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'UHJpbWFyeVNtc0FwaVByb3ZpZGVyLl9wcmVwYXJlX3BheWxvYWQ=').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'UHJpbWFyeVNtc0FwaVByb3ZpZGVy').decode()}`, "
            f"but it was marked as required.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"UHJpbWFyeVNtc0FwaVByb3ZpZGVy").decode(),
            base64.b64decode(
                b"UHJpbWFyeVNtc0FwaVByb3ZpZGVyLl9wcmVwYXJlX3BheWxvYWQ="
            ).decode(),
        )
        self.assertEqual(
            1,
            len(args),
            msg=f"The function "
            f"`{base64.b64decode(b'UHJpbWFyeVNtc0FwaVByb3ZpZGVyLl9wcmVwYXJlX3BheWxvYWQ=').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'UHJpbWFyeVNtc0FwaVByb3ZpZGVy').decode()}` "
            f"should have 1 argument(s).",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"UHJpbWFyeVNtc0FwaVByb3ZpZGVy").decode(),
            base64.b64decode(
                b"UHJpbWFyeVNtc0FwaVByb3ZpZGVyLl9wcmVwYXJlX3BheWxvYWQ="
            ).decode(),
        )
        self.assertEqual(
            base64.b64decode(b"c2VsZg==").decode(),
            args[0],
            msg=f"The argument #0 of function "
            f"`{base64.b64decode(b'UHJpbWFyeVNtc0FwaVByb3ZpZGVyLl9wcmVwYXJlX3BheWxvYWQ=').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'UHJpbWFyeVNtc0FwaVByb3ZpZGVy').decode()}` "
            f"should be called "
            f"`self`.",
        )

    def test_class_function_exists_primarysmsapiprovider__process_response(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"UHJpbWFyeVNtc0FwaVByb3ZpZGVy").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'UHJpbWFyeVNtc0FwaVByb3ZpZGVy').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"UHJpbWFyeVNtc0FwaVByb3ZpZGVy").decode()
        )
        self.assertIn(
            base64.b64decode(
                b"UHJpbWFyeVNtc0FwaVByb3ZpZGVyLl9wcm9jZXNzX3Jlc3BvbnNl"
            ).decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'UHJpbWFyeVNtc0FwaVByb3ZpZGVyLl9wcm9jZXNzX3Jlc3BvbnNl').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'UHJpbWFyeVNtc0FwaVByb3ZpZGVy').decode()}`, "
            f"but it was marked as required.",
        )

    def test_class_function_signature_match_primarysmsapiprovider__process_response(
        self,
    ):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"UHJpbWFyeVNtc0FwaVByb3ZpZGVy").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'UHJpbWFyeVNtc0FwaVByb3ZpZGVy').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"UHJpbWFyeVNtc0FwaVByb3ZpZGVy").decode()
        )
        self.assertIn(
            base64.b64decode(
                b"UHJpbWFyeVNtc0FwaVByb3ZpZGVyLl9wcm9jZXNzX3Jlc3BvbnNl"
            ).decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'UHJpbWFyeVNtc0FwaVByb3ZpZGVyLl9wcm9jZXNzX3Jlc3BvbnNl').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'UHJpbWFyeVNtc0FwaVByb3ZpZGVy').decode()}`, "
            f"but it was marked as required.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"UHJpbWFyeVNtc0FwaVByb3ZpZGVy").decode(),
            base64.b64decode(
                b"UHJpbWFyeVNtc0FwaVByb3ZpZGVyLl9wcm9jZXNzX3Jlc3BvbnNl"
            ).decode(),
        )
        self.assertEqual(
            2,
            len(args),
            msg=f"The function "
            f"`{base64.b64decode(b'UHJpbWFyeVNtc0FwaVByb3ZpZGVyLl9wcm9jZXNzX3Jlc3BvbnNl').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'UHJpbWFyeVNtc0FwaVByb3ZpZGVy').decode()}` "
            f"should have 2 argument(s).",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"UHJpbWFyeVNtc0FwaVByb3ZpZGVy").decode(),
            base64.b64decode(
                b"UHJpbWFyeVNtc0FwaVByb3ZpZGVyLl9wcm9jZXNzX3Jlc3BvbnNl"
            ).decode(),
        )
        self.assertEqual(
            base64.b64decode(b"c2VsZg==").decode(),
            args[0],
            msg=f"The argument #0 of function "
            f"`{base64.b64decode(b'UHJpbWFyeVNtc0FwaVByb3ZpZGVyLl9wcm9jZXNzX3Jlc3BvbnNl').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'UHJpbWFyeVNtc0FwaVByb3ZpZGVy').decode()}` "
            f"should be called "
            f"`self`.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"UHJpbWFyeVNtc0FwaVByb3ZpZGVy").decode(),
            base64.b64decode(
                b"UHJpbWFyeVNtc0FwaVByb3ZpZGVyLl9wcm9jZXNzX3Jlc3BvbnNl"
            ).decode(),
        )
        self.assertEqual(
            base64.b64decode(b"cmVzcA==").decode(),
            args[1],
            msg=f"The argument #1 of function "
            f"`{base64.b64decode(b'UHJpbWFyeVNtc0FwaVByb3ZpZGVyLl9wcm9jZXNzX3Jlc3BvbnNl').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'UHJpbWFyeVNtc0FwaVByb3ZpZGVy').decode()}` "
            f"should be called "
            f"`resp`.",
        )

    def test_class_function_exists_basesmsprovider__validation(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"UHJpbWFyeVNtc0FwaVByb3ZpZGVy").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'UHJpbWFyeVNtc0FwaVByb3ZpZGVy').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"UHJpbWFyeVNtc0FwaVByb3ZpZGVy").decode()
        )
        self.assertIn(
            base64.b64decode(b"QmFzZVNtc1Byb3ZpZGVyLl92YWxpZGF0aW9u").decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'QmFzZVNtc1Byb3ZpZGVyLl92YWxpZGF0aW9u').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'UHJpbWFyeVNtc0FwaVByb3ZpZGVy').decode()}`, "
            f"but it was marked as required.",
        )

    def test_class_function_signature_match_basesmsprovider__validation(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"UHJpbWFyeVNtc0FwaVByb3ZpZGVy").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'UHJpbWFyeVNtc0FwaVByb3ZpZGVy').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"UHJpbWFyeVNtc0FwaVByb3ZpZGVy").decode()
        )
        self.assertIn(
            base64.b64decode(b"QmFzZVNtc1Byb3ZpZGVyLl92YWxpZGF0aW9u").decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'QmFzZVNtc1Byb3ZpZGVyLl92YWxpZGF0aW9u').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'UHJpbWFyeVNtc0FwaVByb3ZpZGVy').decode()}`, "
            f"but it was marked as required.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"UHJpbWFyeVNtc0FwaVByb3ZpZGVy").decode(),
            base64.b64decode(b"QmFzZVNtc1Byb3ZpZGVyLl92YWxpZGF0aW9u").decode(),
        )
        self.assertEqual(
            1,
            len(args),
            msg=f"The function "
            f"`{base64.b64decode(b'QmFzZVNtc1Byb3ZpZGVyLl92YWxpZGF0aW9u').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'UHJpbWFyeVNtc0FwaVByb3ZpZGVy').decode()}` "
            f"should have 1 argument(s).",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"UHJpbWFyeVNtc0FwaVByb3ZpZGVy").decode(),
            base64.b64decode(b"QmFzZVNtc1Byb3ZpZGVyLl92YWxpZGF0aW9u").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"ZnVuYw==").decode(),
            args[0],
            msg=f"The argument #0 of function "
            f"`{base64.b64decode(b'QmFzZVNtc1Byb3ZpZGVyLl92YWxpZGF0aW9u').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'UHJpbWFyeVNtc0FwaVByb3ZpZGVy').decode()}` "
            f"should be called "
            f"`func`.",
        )

    def test_class_function_exists_primarysmsapiprovider_send(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"UHJpbWFyeVNtc0FwaVByb3ZpZGVy").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'UHJpbWFyeVNtc0FwaVByb3ZpZGVy').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"UHJpbWFyeVNtc0FwaVByb3ZpZGVy").decode()
        )
        self.assertIn(
            base64.b64decode(b"UHJpbWFyeVNtc0FwaVByb3ZpZGVyLnNlbmQ=").decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'UHJpbWFyeVNtc0FwaVByb3ZpZGVyLnNlbmQ=').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'UHJpbWFyeVNtc0FwaVByb3ZpZGVy').decode()}`, "
            f"but it was marked as required.",
        )

    def test_class_function_signature_match_primarysmsapiprovider_send(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"UHJpbWFyeVNtc0FwaVByb3ZpZGVy").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'UHJpbWFyeVNtc0FwaVByb3ZpZGVy').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"UHJpbWFyeVNtc0FwaVByb3ZpZGVy").decode()
        )
        self.assertIn(
            base64.b64decode(b"UHJpbWFyeVNtc0FwaVByb3ZpZGVyLnNlbmQ=").decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'UHJpbWFyeVNtc0FwaVByb3ZpZGVyLnNlbmQ=').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'UHJpbWFyeVNtc0FwaVByb3ZpZGVy').decode()}`, "
            f"but it was marked as required.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"UHJpbWFyeVNtc0FwaVByb3ZpZGVy").decode(),
            base64.b64decode(b"UHJpbWFyeVNtc0FwaVByb3ZpZGVyLnNlbmQ=").decode(),
        )
        self.assertEqual(
            1,
            len(args),
            msg=f"The function "
            f"`{base64.b64decode(b'UHJpbWFyeVNtc0FwaVByb3ZpZGVyLnNlbmQ=').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'UHJpbWFyeVNtc0FwaVByb3ZpZGVy').decode()}` "
            f"should have 1 argument(s).",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"UHJpbWFyeVNtc0FwaVByb3ZpZGVy").decode(),
            base64.b64decode(b"UHJpbWFyeVNtc0FwaVByb3ZpZGVyLnNlbmQ=").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"c2VsZg==").decode(),
            args[0],
            msg=f"The argument #0 of function "
            f"`{base64.b64decode(b'UHJpbWFyeVNtc0FwaVByb3ZpZGVyLnNlbmQ=').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'UHJpbWFyeVNtc0FwaVByb3ZpZGVy').decode()}` "
            f"should be called "
            f"`self`.",
        )

    def test_class_function_exists_basesmsprovider_set_content(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"UHJpbWFyeVNtc0FwaVByb3ZpZGVy").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'UHJpbWFyeVNtc0FwaVByb3ZpZGVy').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"UHJpbWFyeVNtc0FwaVByb3ZpZGVy").decode()
        )
        self.assertIn(
            base64.b64decode(b"QmFzZVNtc1Byb3ZpZGVyLnNldF9jb250ZW50").decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'QmFzZVNtc1Byb3ZpZGVyLnNldF9jb250ZW50').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'UHJpbWFyeVNtc0FwaVByb3ZpZGVy').decode()}`, "
            f"but it was marked as required.",
        )

    def test_class_function_signature_match_basesmsprovider_set_content(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"UHJpbWFyeVNtc0FwaVByb3ZpZGVy").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'UHJpbWFyeVNtc0FwaVByb3ZpZGVy').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"UHJpbWFyeVNtc0FwaVByb3ZpZGVy").decode()
        )
        self.assertIn(
            base64.b64decode(b"QmFzZVNtc1Byb3ZpZGVyLnNldF9jb250ZW50").decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'QmFzZVNtc1Byb3ZpZGVyLnNldF9jb250ZW50').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'UHJpbWFyeVNtc0FwaVByb3ZpZGVy').decode()}`, "
            f"but it was marked as required.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"UHJpbWFyeVNtc0FwaVByb3ZpZGVy").decode(),
            base64.b64decode(b"QmFzZVNtc1Byb3ZpZGVyLnNldF9jb250ZW50").decode(),
        )
        self.assertEqual(
            11,
            len(args),
            msg=f"The function "
            f"`{base64.b64decode(b'QmFzZVNtc1Byb3ZpZGVyLnNldF9jb250ZW50').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'UHJpbWFyeVNtc0FwaVByb3ZpZGVy').decode()}` "
            f"should have 11 argument(s).",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"UHJpbWFyeVNtc0FwaVByb3ZpZGVy").decode(),
            base64.b64decode(b"QmFzZVNtc1Byb3ZpZGVyLnNldF9jb250ZW50").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"b2Jq").decode(),
            args[0],
            msg=f"The argument #0 of function "
            f"`{base64.b64decode(b'QmFzZVNtc1Byb3ZpZGVyLnNldF9jb250ZW50').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'UHJpbWFyeVNtc0FwaVByb3ZpZGVy').decode()}` "
            f"should be called "
            f"`obj`.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"UHJpbWFyeVNtc0FwaVByb3ZpZGVy").decode(),
            base64.b64decode(b"QmFzZVNtc1Byb3ZpZGVyLnNldF9jb250ZW50").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"YQ==").decode(),
            args[1],
            msg=f"The argument #1 of function "
            f"`{base64.b64decode(b'QmFzZVNtc1Byb3ZpZGVyLnNldF9jb250ZW50').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'UHJpbWFyeVNtc0FwaVByb3ZpZGVy').decode()}` "
            f"should be called "
            f"`a`.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"UHJpbWFyeVNtc0FwaVByb3ZpZGVy").decode(),
            base64.b64decode(b"QmFzZVNtc1Byb3ZpZGVyLnNldF9jb250ZW50").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"cg==").decode(),
            args[2],
            msg=f"The argument #2 of function "
            f"`{base64.b64decode(b'QmFzZVNtc1Byb3ZpZGVyLnNldF9jb250ZW50').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'UHJpbWFyeVNtc0FwaVByb3ZpZGVy').decode()}` "
            f"should be called "
            f"`r`.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"UHJpbWFyeVNtc0FwaVByb3ZpZGVy").decode(),
            base64.b64decode(b"QmFzZVNtc1Byb3ZpZGVyLnNldF9jb250ZW50").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"Zw==").decode(),
            args[3],
            msg=f"The argument #3 of function "
            f"`{base64.b64decode(b'QmFzZVNtc1Byb3ZpZGVyLnNldF9jb250ZW50').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'UHJpbWFyeVNtc0FwaVByb3ZpZGVy').decode()}` "
            f"should be called "
            f"`g`.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"UHJpbWFyeVNtc0FwaVByb3ZpZGVy").decode(),
            base64.b64decode(b"QmFzZVNtc1Byb3ZpZGVyLnNldF9jb250ZW50").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"cw==").decode(),
            args[4],
            msg=f"The argument #4 of function "
            f"`{base64.b64decode(b'QmFzZVNtc1Byb3ZpZGVyLnNldF9jb250ZW50').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'UHJpbWFyeVNtc0FwaVByb3ZpZGVy').decode()}` "
            f"should be called "
            f"`s`.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"UHJpbWFyeVNtc0FwaVByb3ZpZGVy").decode(),
            base64.b64decode(b"QmFzZVNtc1Byb3ZpZGVyLnNldF9jb250ZW50").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"aw==").decode(),
            args[5],
            msg=f"The argument #5 of function "
            f"`{base64.b64decode(b'QmFzZVNtc1Byb3ZpZGVyLnNldF9jb250ZW50').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'UHJpbWFyeVNtc0FwaVByb3ZpZGVy').decode()}` "
            f"should be called "
            f"`k`.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"UHJpbWFyeVNtc0FwaVByb3ZpZGVy").decode(),
            base64.b64decode(b"QmFzZVNtc1Byb3ZpZGVyLnNldF9jb250ZW50").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"dw==").decode(),
            args[6],
            msg=f"The argument #6 of function "
            f"`{base64.b64decode(b'QmFzZVNtc1Byb3ZpZGVyLnNldF9jb250ZW50').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'UHJpbWFyeVNtc0FwaVByb3ZpZGVy').decode()}` "
            f"should be called "
            f"`w`.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"UHJpbWFyeVNtc0FwaVByb3ZpZGVy").decode(),
            base64.b64decode(b"QmFzZVNtc1Byb3ZpZGVyLnNldF9jb250ZW50").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"YQ==").decode(),
            args[7],
            msg=f"The argument #7 of function "
            f"`{base64.b64decode(b'QmFzZVNtc1Byb3ZpZGVyLnNldF9jb250ZW50').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'UHJpbWFyeVNtc0FwaVByb3ZpZGVy').decode()}` "
            f"should be called "
            f"`a`.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"UHJpbWFyeVNtc0FwaVByb3ZpZGVy").decode(),
            base64.b64decode(b"QmFzZVNtc1Byb3ZpZGVyLnNldF9jb250ZW50").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"cg==").decode(),
            args[8],
            msg=f"The argument #8 of function "
            f"`{base64.b64decode(b'QmFzZVNtc1Byb3ZpZGVyLnNldF9jb250ZW50').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'UHJpbWFyeVNtc0FwaVByb3ZpZGVy').decode()}` "
            f"should be called "
            f"`r`.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"UHJpbWFyeVNtc0FwaVByb3ZpZGVy").decode(),
            base64.b64decode(b"QmFzZVNtc1Byb3ZpZGVyLnNldF9jb250ZW50").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"Zw==").decode(),
            args[9],
            msg=f"The argument #9 of function "
            f"`{base64.b64decode(b'QmFzZVNtc1Byb3ZpZGVyLnNldF9jb250ZW50').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'UHJpbWFyeVNtc0FwaVByb3ZpZGVy').decode()}` "
            f"should be called "
            f"`g`.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"UHJpbWFyeVNtc0FwaVByb3ZpZGVy").decode(),
            base64.b64decode(b"QmFzZVNtc1Byb3ZpZGVyLnNldF9jb250ZW50").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"cw==").decode(),
            args[10],
            msg=f"The argument #10 of function "
            f"`{base64.b64decode(b'QmFzZVNtc1Byb3ZpZGVyLnNldF9jb250ZW50').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'UHJpbWFyeVNtc0FwaVByb3ZpZGVy').decode()}` "
            f"should be called "
            f"`s`.",
        )

    def test_class_function_exists_basesmsprovider_set_recipient(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"UHJpbWFyeVNtc0FwaVByb3ZpZGVy").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'UHJpbWFyeVNtc0FwaVByb3ZpZGVy').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"UHJpbWFyeVNtc0FwaVByb3ZpZGVy").decode()
        )
        self.assertIn(
            base64.b64decode(b"QmFzZVNtc1Byb3ZpZGVyLnNldF9yZWNpcGllbnQ=").decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'QmFzZVNtc1Byb3ZpZGVyLnNldF9yZWNpcGllbnQ=').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'UHJpbWFyeVNtc0FwaVByb3ZpZGVy').decode()}`, "
            f"but it was marked as required.",
        )

    def test_class_function_signature_match_basesmsprovider_set_recipient(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"UHJpbWFyeVNtc0FwaVByb3ZpZGVy").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'UHJpbWFyeVNtc0FwaVByb3ZpZGVy').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"UHJpbWFyeVNtc0FwaVByb3ZpZGVy").decode()
        )
        self.assertIn(
            base64.b64decode(b"QmFzZVNtc1Byb3ZpZGVyLnNldF9yZWNpcGllbnQ=").decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'QmFzZVNtc1Byb3ZpZGVyLnNldF9yZWNpcGllbnQ=').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'UHJpbWFyeVNtc0FwaVByb3ZpZGVy').decode()}`, "
            f"but it was marked as required.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"UHJpbWFyeVNtc0FwaVByb3ZpZGVy").decode(),
            base64.b64decode(b"QmFzZVNtc1Byb3ZpZGVyLnNldF9yZWNpcGllbnQ=").decode(),
        )
        self.assertEqual(
            11,
            len(args),
            msg=f"The function "
            f"`{base64.b64decode(b'QmFzZVNtc1Byb3ZpZGVyLnNldF9yZWNpcGllbnQ=').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'UHJpbWFyeVNtc0FwaVByb3ZpZGVy').decode()}` "
            f"should have 11 argument(s).",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"UHJpbWFyeVNtc0FwaVByb3ZpZGVy").decode(),
            base64.b64decode(b"QmFzZVNtc1Byb3ZpZGVyLnNldF9yZWNpcGllbnQ=").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"b2Jq").decode(),
            args[0],
            msg=f"The argument #0 of function "
            f"`{base64.b64decode(b'QmFzZVNtc1Byb3ZpZGVyLnNldF9yZWNpcGllbnQ=').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'UHJpbWFyeVNtc0FwaVByb3ZpZGVy').decode()}` "
            f"should be called "
            f"`obj`.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"UHJpbWFyeVNtc0FwaVByb3ZpZGVy").decode(),
            base64.b64decode(b"QmFzZVNtc1Byb3ZpZGVyLnNldF9yZWNpcGllbnQ=").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"YQ==").decode(),
            args[1],
            msg=f"The argument #1 of function "
            f"`{base64.b64decode(b'QmFzZVNtc1Byb3ZpZGVyLnNldF9yZWNpcGllbnQ=').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'UHJpbWFyeVNtc0FwaVByb3ZpZGVy').decode()}` "
            f"should be called "
            f"`a`.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"UHJpbWFyeVNtc0FwaVByb3ZpZGVy").decode(),
            base64.b64decode(b"QmFzZVNtc1Byb3ZpZGVyLnNldF9yZWNpcGllbnQ=").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"cg==").decode(),
            args[2],
            msg=f"The argument #2 of function "
            f"`{base64.b64decode(b'QmFzZVNtc1Byb3ZpZGVyLnNldF9yZWNpcGllbnQ=').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'UHJpbWFyeVNtc0FwaVByb3ZpZGVy').decode()}` "
            f"should be called "
            f"`r`.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"UHJpbWFyeVNtc0FwaVByb3ZpZGVy").decode(),
            base64.b64decode(b"QmFzZVNtc1Byb3ZpZGVyLnNldF9yZWNpcGllbnQ=").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"Zw==").decode(),
            args[3],
            msg=f"The argument #3 of function "
            f"`{base64.b64decode(b'QmFzZVNtc1Byb3ZpZGVyLnNldF9yZWNpcGllbnQ=').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'UHJpbWFyeVNtc0FwaVByb3ZpZGVy').decode()}` "
            f"should be called "
            f"`g`.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"UHJpbWFyeVNtc0FwaVByb3ZpZGVy").decode(),
            base64.b64decode(b"QmFzZVNtc1Byb3ZpZGVyLnNldF9yZWNpcGllbnQ=").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"cw==").decode(),
            args[4],
            msg=f"The argument #4 of function "
            f"`{base64.b64decode(b'QmFzZVNtc1Byb3ZpZGVyLnNldF9yZWNpcGllbnQ=').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'UHJpbWFyeVNtc0FwaVByb3ZpZGVy').decode()}` "
            f"should be called "
            f"`s`.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"UHJpbWFyeVNtc0FwaVByb3ZpZGVy").decode(),
            base64.b64decode(b"QmFzZVNtc1Byb3ZpZGVyLnNldF9yZWNpcGllbnQ=").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"aw==").decode(),
            args[5],
            msg=f"The argument #5 of function "
            f"`{base64.b64decode(b'QmFzZVNtc1Byb3ZpZGVyLnNldF9yZWNpcGllbnQ=').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'UHJpbWFyeVNtc0FwaVByb3ZpZGVy').decode()}` "
            f"should be called "
            f"`k`.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"UHJpbWFyeVNtc0FwaVByb3ZpZGVy").decode(),
            base64.b64decode(b"QmFzZVNtc1Byb3ZpZGVyLnNldF9yZWNpcGllbnQ=").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"dw==").decode(),
            args[6],
            msg=f"The argument #6 of function "
            f"`{base64.b64decode(b'QmFzZVNtc1Byb3ZpZGVyLnNldF9yZWNpcGllbnQ=').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'UHJpbWFyeVNtc0FwaVByb3ZpZGVy').decode()}` "
            f"should be called "
            f"`w`.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"UHJpbWFyeVNtc0FwaVByb3ZpZGVy").decode(),
            base64.b64decode(b"QmFzZVNtc1Byb3ZpZGVyLnNldF9yZWNpcGllbnQ=").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"YQ==").decode(),
            args[7],
            msg=f"The argument #7 of function "
            f"`{base64.b64decode(b'QmFzZVNtc1Byb3ZpZGVyLnNldF9yZWNpcGllbnQ=').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'UHJpbWFyeVNtc0FwaVByb3ZpZGVy').decode()}` "
            f"should be called "
            f"`a`.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"UHJpbWFyeVNtc0FwaVByb3ZpZGVy").decode(),
            base64.b64decode(b"QmFzZVNtc1Byb3ZpZGVyLnNldF9yZWNpcGllbnQ=").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"cg==").decode(),
            args[8],
            msg=f"The argument #8 of function "
            f"`{base64.b64decode(b'QmFzZVNtc1Byb3ZpZGVyLnNldF9yZWNpcGllbnQ=').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'UHJpbWFyeVNtc0FwaVByb3ZpZGVy').decode()}` "
            f"should be called "
            f"`r`.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"UHJpbWFyeVNtc0FwaVByb3ZpZGVy").decode(),
            base64.b64decode(b"QmFzZVNtc1Byb3ZpZGVyLnNldF9yZWNpcGllbnQ=").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"Zw==").decode(),
            args[9],
            msg=f"The argument #9 of function "
            f"`{base64.b64decode(b'QmFzZVNtc1Byb3ZpZGVyLnNldF9yZWNpcGllbnQ=').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'UHJpbWFyeVNtc0FwaVByb3ZpZGVy').decode()}` "
            f"should be called "
            f"`g`.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"UHJpbWFyeVNtc0FwaVByb3ZpZGVy").decode(),
            base64.b64decode(b"QmFzZVNtc1Byb3ZpZGVyLnNldF9yZWNpcGllbnQ=").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"cw==").decode(),
            args[10],
            msg=f"The argument #10 of function "
            f"`{base64.b64decode(b'QmFzZVNtc1Byb3ZpZGVyLnNldF9yZWNpcGllbnQ=').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'UHJpbWFyeVNtc0FwaVByb3ZpZGVy').decode()}` "
            f"should be called "
            f"`s`.",
        )


# === Internal functions, do not modify ===
import inspect

from types import ModuleType
from typing import List


def _get_function_names(module: ModuleType) -> List[str]:
    names = []
    functions = inspect.getmembers(module, lambda member: inspect.isfunction(member))
    for name, fn in functions:
        if fn.__module__ == module.__name__:
            names.append(name)
    return names


def _get_function_arg_names(module: ModuleType, fn_name: str) -> List[str]:
    arg_names = []
    functions = inspect.getmembers(module, lambda member: inspect.isfunction(member))
    for name, fn in functions:
        if fn.__module__ == module.__name__:
            if fn.__qualname__ == fn_name:
                args_spec = inspect.getfullargspec(fn)
                arg_names = args_spec.args
                if args_spec.varargs is not None:
                    arg_names.extend(args_spec.varargs)
                if args_spec.varkw is not None:
                    arg_names.extend(args_spec.varkw)
                arg_names.extend(args_spec.kwonlyargs)
                break
    return arg_names


def _get_class_names(module: ModuleType) -> List[str]:
    names = []
    classes = inspect.getmembers(module, lambda member: inspect.isclass(member))
    for name, cls in classes:
        if cls.__module__ == module.__name__:
            names.append(name)
    return names


def _get_class_function_names(module: ModuleType, cls_name: str) -> List[str]:
    fn_names = []
    classes = inspect.getmembers(module, lambda member: inspect.isclass(member))
    for cls_name_, cls in classes:
        if cls.__module__ == module.__name__:
            if cls_name_ == cls_name:
                functions = inspect.getmembers(
                    cls,
                    lambda member: inspect.ismethod(member)
                    or inspect.isfunction(member),
                )
                for fn_name, fn in functions:
                    fn_names.append(fn.__qualname__)
                break
    return fn_names


def _get_class_function_arg_names(
    module: ModuleType, cls_name: str, fn_name: str
) -> List[str]:
    arg_names = []
    classes = inspect.getmembers(module, lambda member: inspect.isclass(member))
    for cls_name_, cls in classes:
        if cls.__module__ == module.__name__:
            if cls_name_ == cls_name:
                functions = inspect.getmembers(
                    cls,
                    lambda member: inspect.ismethod(member)
                    or inspect.isfunction(member),
                )
                for fn_name_, fn in functions:
                    if fn.__qualname__ == fn_name:
                        args_spec = inspect.getfullargspec(fn)
                        arg_names = args_spec.args
                        if args_spec.varargs is not None:
                            arg_names.extend(args_spec.varargs)
                        if args_spec.varkw is not None:
                            arg_names.extend(args_spec.varkw)
                        arg_names.extend(args_spec.kwonlyargs)
                        break
                break
    return arg_names
