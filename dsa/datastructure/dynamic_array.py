from typing import Generic, List, Optional, TypeVar
from collections.abc import Iterator, Iterable

from .static_array import StaticArray

T = TypeVar("T")


class DynamicArray(StaticArray[T], Generic[T]):
    size: int
    ratio: int
    upper: int
    lower: int

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
        self._copy_forward(0, n, arr, 0)
        self.arr = arr
        self._compute_bounds()

    def __len__(self) -> int:
        return self.size

    def __iter__(self) -> Iterator[T]:
        for i in range(self.size):
            element = self.arr[i]
            assert element is not None
            yield element

    def build(self, X: Iterable[T]) -> None:
        for x in X:
            self.insert_last(x)

    def get_at(self, i: int) -> T:
        if i >= len(self):
            raise IndexError("list index out of range")
        return super().get_at(i)

    def set_at(self, i: int, x: T) -> None:
        if i >= len(self):
            raise IndexError("list index out of range")
        return super().set_at(i, x)

    def insert_last(self, x: Optional[T]) -> None:
        self._resize(len(self) + 1)
        self.arr[len(self)] = x
        self.size += 1

    def delete_last(self) -> T:
        if len(self) == 0:
            raise IndexError("list index out of range")
        x = self.arr[self.size - 1]
        assert x is not None
        self.size -= 1
        self._resize(self.size)
        return x

    def insert_at(self, i: int, x: T) -> None:
        self.insert_last(None)
        self._copy_backward(i, self.size - 1 - i, self.arr, i + 1)
        self.arr[i] = x

    def delete_at(self, i: int) -> T:
        if i >= len(self):
            raise IndexError("list index out of range")
        x = self.arr[i]
        assert x is not None
        self._copy_forward(i + 1, self.size - (i + 1), self.arr, i)
        self.delete_last()
        return x

    def insert_first(self, x: T) -> None:
        return self.insert_at(0, x)

    def delete_first(self) -> T:
        return self.delete_at(0)
