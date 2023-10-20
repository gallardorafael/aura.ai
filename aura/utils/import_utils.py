import importlib.metadata
import importlib.util
from typing import Tuple, Union


# TODO: This doesn't work for all packages (`bs4`, `faiss`, etc.)
def _is_package_available(pkg_name: str, return_version: bool = False) -> Union[Tuple[bool, str], bool]:
    """Taken from: https://github.com/huggingface/transformers/blob/main/src/transformers/utils/imp
    ort_utils.py."""
    # Check we're not importing a "pkg_name" directory somewhere but the actual library by trying to grab the version
    package_exists = importlib.util.find_spec(pkg_name) is not None
    package_version = "N/A"
    if package_exists:
        try:
            package_version = importlib.metadata.version(pkg_name)
            package_exists = True
        except importlib.metadata.PackageNotFoundError:
            package_exists = False
    if return_version:
        return package_exists, package_version
    else:
        return package_exists


# getting availability of packages
_torch_available, _torch_version = _is_package_available("torch", return_version=True)


def is_torch_available():
    return _torch_available


def get_torch_version():
    return _torch_version
