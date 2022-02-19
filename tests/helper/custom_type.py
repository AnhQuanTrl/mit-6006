from typing import Generic, TypeVar
from pytest import FixtureRequest as _FixtureRequest

T = TypeVar("T")


class FixtureRequest(_FixtureRequest, Generic[T]):
    param: T
