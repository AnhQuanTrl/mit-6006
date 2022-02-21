from abc import ABC, abstractmethod
from typing import Generic, Sized, TypeVar
from collections.abc import Iterable

T = TypeVar("T")


class Sequence(ABC, Sized, Iterable[T], Generic[T]):
    @abstractmethod
    def build(self, X: Iterable[T]) -> None:
        pass

    @abstractmethod
    def get_at(self, i: int) -> T:
        pass

    @abstractmethod
    def set_at(self, i: int, x: T) -> None:
        pass

    @abstractmethod
    def insert_at(self, i: int, x: T) -> None:
        pass

    @abstractmethod
    def delete_at(self, i: int) -> T:
        pass

    @abstractmethod
    def insert_first(self, x: T) -> None:
        pass

    @abstractmethod
    def delete_first(self) -> T:
        pass

    @abstractmethod
    def insert_last(self, x: T) -> None:
        pass

    @abstractmethod
    def delete_last(self) -> T:
        pass
