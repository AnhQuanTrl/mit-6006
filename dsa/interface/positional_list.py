from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Generic, Optional, Sized, TypeVar
from collections.abc import Iterable


T = TypeVar("T")


class Position(ABC, Generic[T]):
    @property
    @abstractmethod
    def element(self) -> T:
        pass

    @element.setter
    @abstractmethod
    def element(self, x: T) -> None:
        pass

    @abstractmethod
    def __eq__(self, __o: object) -> bool:
        pass

    @abstractmethod
    def __ne__(self, __o: object) -> bool:
        pass


class PositionalList(ABC, Sized, Iterable[T], Generic[T]):
    @abstractmethod
    def build(self, X: Iterable[T]) -> None:
        pass

    @abstractmethod
    def first(self) -> Optional[Position[T]]:
        pass

    @abstractmethod
    def last(self) -> Optional[Position[T]]:
        pass

    @abstractmethod
    def before(self, p: Position[T]) -> Optional[Position[T]]:
        pass

    @abstractmethod
    def after(self, p: Position[T]) -> Optional[Position[T]]:
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        pass

    @abstractmethod
    def add_first(self, e: T) -> Position[T]:
        pass

    @abstractmethod
    def add_last(self, e: T) -> Position[T]:
        pass

    @abstractmethod
    def add_before(self, p: Position[T], e: T) -> Position[T]:
        pass

    @abstractmethod
    def add_after(self, p: Position[T], e: T) -> Position[T]:
        pass

    @abstractmethod
    def delete(self, p: Position[T]) -> T:
        pass
