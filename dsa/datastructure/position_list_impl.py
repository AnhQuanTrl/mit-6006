from __future__ import annotations
from typing import Generic, Optional, TypeVar
from collections.abc import Iterator, Iterable
from dsa.datastructure.doubly_linked_list import DoublyLinkedList, DoublyLinkedListNode

from dsa.interface.positional_list import Position, PositionalList


T = TypeVar("T")


class PositionImpl(Position[T], Generic[T]):
    node: DoublyLinkedListNode[T]
    container: PositionalListImpl[T]

    def __init__(
        self, node: DoublyLinkedListNode[T], container: PositionalListImpl[T]
    ) -> None:
        self.node = node
        self.container = container

    @property
    def element(self) -> T:
        assert self.node.item is not None
        return self.node.item

    @element.setter
    def element(self, x: T) -> None:
        self.node.item = x

    def __eq__(self, __o: object) -> bool:
        return type(__o) is type(self) and __o.node is self.node

    def __ne__(self, __o: object) -> bool:
        return not (self == __o)


class PositionalListImpl(DoublyLinkedList[T], PositionalList[T], Generic[T]):
    def __init__(self) -> None:
        super().__init__()

    def build(self, X: Iterable[T]) -> None:
        return super().build(X)

    def first(self) -> Optional[Position[T]]:
        return self._make_position(self.head)

    def last(self) -> Optional[Position[T]]:
        return self._make_position(self.tail)

    def before(self, p: Position[T]) -> Optional[Position[T]]:
        node = self._validate(p)
        return self._make_position(node.prev)

    def after(self, p: Position[T]) -> Optional[Position[T]]:
        node = self._validate(p)
        return self._make_position(node.next)

    def __len__(self) -> int:
        return self.size

    def is_empty(self) -> bool:
        return len(self) == 0

    def __iter__(self) -> Iterator[T]:
        pos = self.first()
        while pos:
            yield pos.element
            pos = self.after(pos)

    def add_first(self, e: T) -> Position[T]:
        assert self.header.next
        return self._insert_position_between(e, self.header, self.header.next)

    def add_last(self, e: T) -> Position[T]:
        assert self.trailer.prev
        return self._insert_position_between(e, self.trailer.prev, self.trailer)

    def add_before(self, p: Position[T], e: T) -> Position[T]:
        node = self._validate(p)
        assert node.prev
        return self._insert_position_between(e, node.prev, node)

    def add_after(self, p: Position[T], e: T) -> Position[T]:
        node = self._validate(p)
        assert node.next
        return self._insert_position_between(e, node, node.next)

    def delete(self, p: Position[T]) -> T:
        original = self._validate(p)
        return self._delete_node(original)

    def _make_position(
        self, node: Optional[DoublyLinkedListNode[T]]
    ) -> Optional[PositionImpl[T]]:
        if not node or node is self.header or node is self.trailer:
            return None
        return PositionImpl(node, self)

    def _validate(self, p: Position[T]) -> DoublyLinkedListNode[T]:
        if not isinstance(p, PositionImpl):
            raise TypeError("p must be proper position type")
        if p.container is not self:
            raise ValueError("p does not belong to this container")
        if p.node.next is None:
            raise ValueError("p is no longer valid")
        return p.node

    def _insert_position_between(
        self,
        x: T,
        predecessor: DoublyLinkedListNode[T],
        successor: DoublyLinkedListNode[T],
    ) -> Position[T]:
        node = super()._insert_between(x, predecessor, successor)
        position = self._make_position(node)
        assert position is not None
        return position
