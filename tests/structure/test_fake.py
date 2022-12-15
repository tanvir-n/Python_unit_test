import base64
import unittest

import app.fake


class StructureTestSuite(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.MODULE = app.fake

    def test_function_exists_fake_primary_external_api(self):
        functions = _get_function_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"ZmFrZV9wcmltYXJ5X2V4dGVybmFsX2FwaQ==").decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'ZmFrZV9wcmltYXJ5X2V4dGVybmFsX2FwaQ==').decode()}` "
            f"is not found, but it was marked as required.",
        )

    def test_function_signature_match_fake_primary_external_api(self):
        functions = _get_function_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"ZmFrZV9wcmltYXJ5X2V4dGVybmFsX2FwaQ==").decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'ZmFrZV9wcmltYXJ5X2V4dGVybmFsX2FwaQ==').decode()}` "
            f"is not found, but it was marked as required.",
        )
        args = _get_function_arg_names(
            self.MODULE,
            base64.b64decode(b"ZmFrZV9wcmltYXJ5X2V4dGVybmFsX2FwaQ==").decode(),
        )
        self.assertEqual(
            1,
            len(args),
            msg=f"The function "
            f"`{base64.b64decode(b'ZmFrZV9wcmltYXJ5X2V4dGVybmFsX2FwaQ==').decode()}` "
            f"should have exactly 1 argument(s).",
        )
        args = _get_function_arg_names(
            self.MODULE,
            base64.b64decode(b"ZmFrZV9wcmltYXJ5X2V4dGVybmFsX2FwaQ==").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"bWVzc2FnZQ==").decode(),
            args[0],
            msg=f"The argument #0 of function "
            f"`{base64.b64decode(b'ZmFrZV9wcmltYXJ5X2V4dGVybmFsX2FwaQ==').decode()}` "
            f"should be called "
            f"`message`.",
        )

    def test_function_exists_fake_secondary_external_api(self):
        functions = _get_function_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"ZmFrZV9zZWNvbmRhcnlfZXh0ZXJuYWxfYXBp").decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'ZmFrZV9zZWNvbmRhcnlfZXh0ZXJuYWxfYXBp').decode()}` "
            f"is not found, but it was marked as required.",
        )

    def test_function_signature_match_fake_secondary_external_api(self):
        functions = _get_function_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"ZmFrZV9zZWNvbmRhcnlfZXh0ZXJuYWxfYXBp").decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'ZmFrZV9zZWNvbmRhcnlfZXh0ZXJuYWxfYXBp').decode()}` "
            f"is not found, but it was marked as required.",
        )
        args = _get_function_arg_names(
            self.MODULE,
            base64.b64decode(b"ZmFrZV9zZWNvbmRhcnlfZXh0ZXJuYWxfYXBp").decode(),
        )
        self.assertEqual(
            1,
            len(args),
            msg=f"The function "
            f"`{base64.b64decode(b'ZmFrZV9zZWNvbmRhcnlfZXh0ZXJuYWxfYXBp').decode()}` "
            f"should have exactly 1 argument(s).",
        )
        args = _get_function_arg_names(
            self.MODULE,
            base64.b64decode(b"ZmFrZV9zZWNvbmRhcnlfZXh0ZXJuYWxfYXBp").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"bWVzc2FnZQ==").decode(),
            args[0],
            msg=f"The argument #0 of function "
            f"`{base64.b64decode(b'ZmFrZV9zZWNvbmRhcnlfZXh0ZXJuYWxfYXBp').decode()}` "
            f"should be called "
            f"`message`.",
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
