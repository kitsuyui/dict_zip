import importlib

import dict_zip


def test_star_import_resolves_all_entries() -> None:
    namespace: dict[str, object] = {}
    exec("from dict_zip import *", namespace)  # noqa: S102

    for name in dict_zip.__all__:
        assert name in namespace, (
            f"{name} listed in __all__ but missing from import *"
        )


def test_all_entries_are_attributes() -> None:
    module = importlib.import_module("dict_zip")
    for name in module.__all__:
        assert hasattr(module, name), (
            f"{name} listed in __all__ but not defined on module"
        )
