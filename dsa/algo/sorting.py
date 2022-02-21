from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Generic, List, TypeVar, Protocol


T = TypeVar("T", bound="Comparable")


class Comparable(Protocol):
    def __lt__(self: T, __x: T) -> bool:
        ...


class Sort(ABC, Generic[T]):
    @abstractmethod
    def sort(self, data: List[T]) -> None:
        pass


class BubbleSort(Sort[T], Generic[T]):
    def sort(self, data: List[T]) -> None:
        n = len(data)
        for i in range(n):
            for j in range(n - 1 - i):
                if data[j + 1] < data[j]:
                    data[j], data[j + 1] = data[j + 1], data[j]


class SelectionSort(Sort[T], Generic[T]):
    def sort(self, data: List[T]) -> None:
        n = len(data)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if data[j] < data[min_index]:
                    min_index = j
            data[i], data[min_index] = data[min_index], data[i]
