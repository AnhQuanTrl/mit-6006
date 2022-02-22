from typing import Generic, List, Optional, TypeVar
from dsa.interface.queue import EmptyQueueException, Queue

T = TypeVar("T")


class ArrayQueue(Queue[T], Generic[T]):
    arr: List[Optional[T]]
    head: int
    size: int
    ratio: int
    upper: int
    lower: int

    def __init__(self, ratio: int = 2) -> None:
        self.arr = []
        self.head = 0
        self.size = 0
        self.ratio = ratio
        self._compute_bounds()
        self._resize(0)

    def _compute_bounds(self):
        self.upper = len(self.arr)
        self.lower = len(self.arr) // (self.ratio * self.ratio)

    def _resize(self, n: int):
        if self.lower < n < self.upper:
            return
        m = max(n, 1) * self.ratio
        arr: List[Optional[T]] = [None] * m
        self._copy(arr)
        self.arr = arr
        self.head = 0
        self._compute_bounds()

    def _copy(self, arr: List[Optional[T]]):
        n = self.size
        for i in range(n):
            index: int = (self.head + i) % len(self.arr)
            arr[i] = self.arr[index]

    def enqueue(self, item: T) -> None:
        self._resize(self.size + 1)
        self.arr[(self.head + self.size) % len(self.arr)] = item
        self.size += 1

    def dequeue(self) -> T:
        if self.is_empty():
            raise EmptyQueueException()
        x = self.arr[self.head]
        assert x is not None
        self.arr[self.head] = None
        self.head += 1
        self.size -= 1
        self._resize(self.size)
        return x

    def peek(self) -> Optional[T]:
        return self.arr[self.head] if self.size else None

    def is_empty(self) -> bool:
        return self.size == 0
