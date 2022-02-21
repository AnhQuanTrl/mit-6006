from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar
from collections.abc import Iterable, Iterator


T = TypeVar("T")


class Stack(ABC, Iterable[T], Generic[T]):
    def build(self, X: Iterable[T]) -> None:
        for x in X:
            self.push(x)

    @abstractmethod
    def peek(self) -> Optional[T]:
        pass

    @abstractmethod
    def pop(self) -> T:
        pass

    @abstractmethod
    def push(self, item: T) -> None:
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        pass

    def __iter__(self) -> Iterator[T]:
        while not self.is_empty():
            yield self.pop()


class StackUnderflowException(Exception):
    def __init__(
        self, msg: str = "Stack is underflowed", *args: object, **kwargs: object
    ) -> None:
        super().__init__(msg, *args, **kwargs)
