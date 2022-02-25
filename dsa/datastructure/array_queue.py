from typing import Generic, Optional, TypeVar
from dsa.datastructure.circular_array import CircularArray
from dsa.interface.queue import EmptyQueueException, Queue

T = TypeVar("T")


class ArrayQueue(Queue[T], Generic[T]):
    arr: CircularArray[T]

    def __init__(self, ratio: int = 2) -> None:
        self.arr = CircularArray()

    def enqueue(self, item: T) -> None:
        self.arr.insert_last(item)

    def dequeue(self) -> T:
        try:
            x = self.arr.delete_first()
        except IndexError:
            raise EmptyQueueException()
        return x

    def peek(self) -> Optional[T]:
        try:
            x = self.arr.get_at(0)
        except IndexError:
            x = None
        return x

    def is_empty(self) -> bool:
        return len(self.arr) == 0
