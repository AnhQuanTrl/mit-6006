from typing import Generic, List, Optional, TypeVar
from collections.abc import Iterator, Iterable

from dsa.datastructure.static_array import StaticArray


T = TypeVar("T")


class CircularArray(StaticArray[T], Generic[T]):
    head: int

    def __init__(self, ratio: int = 2):
        super().__init__()
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
            index: int = self._compute_index(i)
            arr[i] = self.arr[index]

    def __len__(self) -> int:
        return self.size

    def __iter__(self) -> Iterator[T]:
        for i in range(self.size):
            element = self.arr[self._compute_index(i)]
            assert element is not None
            yield element

    def build(self, X: Iterable[T]) -> None:
        for x in X:
            self.insert_last(x)

    def insert_last(self, x: Optional[T]) -> None:
        self._resize(self.size + 1)
        self.arr[self._compute_index(self.size)] = x
        self.size += 1

    def insert_first(self, x: T) -> None:
        self._resize(self.size + 1)
        index = self._compute_index(-1)
        self.arr[index] = x
        self.size += 1
        self.head = index

    def delete_first(self) -> T:
        if self.size == 0:
            raise IndexError("list index out of range")
        x = self.arr[self.head]
        assert x is not None
        self.arr[self.head] = None
        self.head = self._compute_index(1)
        self.size -= 1
        self._resize(self.size)
        return x

    def delete_last(self) -> T:
        if self.size == 0:
            raise IndexError("list index out of range")
        index = self._compute_index(self.size - 1)
        x = self.arr[index]
        assert x is not None
        self.arr[index] = None
        self.size -= 1
        self._resize(self.size)
        return x

    def get_at(self, i: int) -> T:
        if i >= len(self):
            raise IndexError("list index out of range")
        return super().get_at(self._compute_index(i))

    def set_at(self, i: int, x: T) -> None:
        if i >= len(self):
            raise IndexError("list index out of range")
        return super().set_at(self._compute_index(i), x)

    def insert_at(self, i: int, x: T) -> None:
        self.insert_last(None)
        n = len(self)
        for j in range(n - 1, i, -1):
            self.arr[self._compute_index(j)] = self.arr[self._compute_index(j - 1)]
        self.arr[self._compute_index(i)] = x

    def delete_at(self, i: int) -> T:
        if i >= len(self):
            raise IndexError("list index out of range")
        x = self.arr[self._compute_index(i)]
        assert x is not None
        n = len(self)
        for j in range(i, n - 1):
            self.arr[self._compute_index(j)] = self.arr[self._compute_index(j + 1)]
        self.delete_last()
        return x

    def _compute_index(self, i: int) -> int:
        return (self.head + i) % len(self.arr)
