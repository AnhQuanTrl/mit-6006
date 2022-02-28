from typing import Generic, TypeVar
from dsa.datastructure.circular_array import CircularArray
from dsa.interface.deque import EmptyDequeException
from dsa.interface.deque import Deque


T = TypeVar("T")


class CircularArrayDeque(Deque[T], Generic[T]):
    arr: CircularArray[T]

    def __init__(self) -> None:
        self.arr = CircularArray()

    def add_first(self, item: T) -> None:
        self.arr.insert_first(item)

    def add_last(self, item: T) -> None:
        self.arr.insert_last(item)

    def remove_first(self) -> T:
        try:
            return self.arr.delete_first()
        except IndexError:
            raise EmptyDequeException()

    def remove_last(self) -> T:
        try:
            return self.arr.delete_last()
        except IndexError:
            raise EmptyDequeException()

    def is_empty(self) -> bool:
        return len(self.arr) == 0
