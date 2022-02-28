from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from collections.abc import Iterable, Iterator


T = TypeVar("T")


class Deque(ABC, Generic[T]):
    def build(self, X: Iterable[T]) -> None:
        for x in X:
            self.add_last(x)

    @abstractmethod
    def add_first(self, item: T) -> None:
        pass

    @abstractmethod
    def add_last(self, item: T) -> None:
        pass

    @abstractmethod
    def remove_first(self) -> T:
        pass

    @abstractmethod
    def remove_last(self) -> T:
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        pass

    def __iter__(self) -> Iterator[T]:
        while not self.is_empty():
            yield self.remove_first()


class EmptyDequeException(Exception):
    def __init__(self, msg: str = "deque is empty", *args: object) -> None:
        super().__init__(msg, *args)
