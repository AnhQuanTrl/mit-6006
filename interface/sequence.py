from abc import ABC, abstractmethod
from typing import Generic, TypeVar
from collections.abc import Iterable, Iterator

T = TypeVar("T")


class Sequence(ABC, Generic[T]):
    @abstractmethod
    def build(self, X: Iterable[T]) -> None:
        pass

    @abstractmethod
    def __len__(self) -> int:
        pass

    @abstractmethod
    def __iter__(self) -> Iterator[T]:
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
