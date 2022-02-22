from abc import ABC, abstractmethod
from typing import Generic, Iterable, Optional, TypeVar
from collections.abc import Iterator

T = TypeVar("T")


class Queue(ABC, Generic[T]):
    def build(self, X: Iterable[T]) -> None:
        for x in X:
            self.enqueue(x)

    @abstractmethod
    def peek(self) -> Optional[T]:
        pass

    @abstractmethod
    def enqueue(self, item: T) -> None:
        pass

    @abstractmethod
    def dequeue(self) -> T:
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        pass

    def __iter__(self) -> Iterator[T]:
        while not self.is_empty():
            yield self.dequeue()


class EmptyQueueException(Exception):
    def __init__(self, msg: str = "queue is empty", *args: object) -> None:
        super().__init__(msg, *args)
