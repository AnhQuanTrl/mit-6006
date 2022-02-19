from typing import Generic, List, Optional, TypeVar, cast
from collections.abc import Iterator, Iterable
from dsa.interface.sequence import Sequence

T = TypeVar("T")


class StaticArray(Sequence[T], Generic[T]):
    def __init__(self):
        self.arr: List[T] = []
        self.size: int = 0

    def __len__(self) -> int:
        return self.size

    def __iter__(self) -> Iterator[T]:
        yield from self.arr

    def build(self, X: Iterable[T]) -> None:
        self.arr = [a for a in X]
        self.size = len(self.arr)

    def get_at(self, i: int) -> T:
        return self.arr[i]

    def set_at(self, i: int, x: T) -> None:
        self.arr[i] = x

    def insert_at(self, i: int, x: T) -> None:
        n = len(self)
        arr: List[Optional[T]] = [None] * (n + 1)
        self._copy_forward(0, i, arr, 0)
        arr[i] = x
        self._copy_forward(i, n - i, arr, i + 1)
        self.build(cast(List[T], arr))

    def delete_at(self, i: int) -> T:
        n = len(self)
        arr: List[Optional[T]] = [None] * (n - 1)
        self._copy_forward(0, i, arr, 0)
        self._copy_forward(i + 1, n - i - 1, arr, i)
        x = self.get_at(i)
        self.build(cast(List[T], arr))
        return x

    def insert_first(self, x: T) -> None:
        self.insert_at(0, x)

    def insert_last(self, x: T) -> None:
        self.insert_at(len(self), x)

    def delete_first(self) -> T:
        return self.delete_at(0)

    def delete_last(self) -> T:
        return self.delete_at(len(self) - 1)

    def _copy_backward(self, i: int, n: int, arr: List[Optional[T]], j: int):
        for k in range(n - 1, -1, -1):
            arr[j + k] = self.arr[i + k]

    def _copy_forward(self, i: int, n: int, arr: list[Optional[T]], j: int):
        for k in range(n):
            arr[j + k] = self.arr[i + k]
