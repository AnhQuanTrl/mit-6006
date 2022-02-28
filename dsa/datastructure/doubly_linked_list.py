from __future__ import annotations
from typing import Generic, Optional, TypeVar
from collections.abc import Iterator, Iterable

from dsa.interface.sequence import Sequence


T = TypeVar("T")


class DoublyLinkedListNode(Generic[T]):
    item: Optional[T]
    next: Optional[DoublyLinkedListNode[T]]
    prev: Optional[DoublyLinkedListNode[T]]

    def __init__(
        self,
        __x: Optional[T] = None,
        next: Optional[DoublyLinkedListNode[T]] = None,
        prev: Optional[DoublyLinkedListNode[T]] = None,
    ):
        self.item = __x
        self.next = next
        self.prev = prev

    def later_node(self, i: int) -> DoublyLinkedListNode[T]:
        if i == 0:
            return self
        assert self.next
        return self.next.later_node(i - 1)

    def previous_node(self, i: int) -> DoublyLinkedListNode[T]:
        if i == 0:
            return self
        assert self.prev
        return self.prev.previous_node(i - 1)


class DoublyLinkedList(Sequence[T], Generic[T]):
    header: DoublyLinkedListNode[T]
    trailer: DoublyLinkedListNode[T]
    size: int

    def __init__(self) -> None:
        self.header = self.trailer = DoublyLinkedListNode()
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0

    def __len__(self) -> int:
        return self.size

    def __iter__(self) -> Iterator[T]:
        node = self.head
        while node != self.trailer:
            assert node
            assert node.item is not None
            yield node.item
            node = node.next

    @property
    def head(self) -> Optional[DoublyLinkedListNode[T]]:
        return self.header.next

    @property
    def tail(self) -> Optional[DoublyLinkedListNode[T]]:
        return self.trailer.prev

    def build(self, X: Iterable[T]) -> None:
        self._clear()
        for x in X:
            self.insert_last(x)

    def insert_first(self, x: T) -> None:
        assert self.header.next
        return self._insert_between(x, self.header, self.header.next)

    def insert_last(self, x: T) -> None:
        assert self.trailer.prev
        return self._insert_between(x, self.trailer.prev, self.trailer)

    def delete_first(self) -> T:
        if self.size == 0:
            raise IndexError("list index out of range")
        assert self.header.next
        return self._delete(self.header.next)

    def delete_last(self) -> T:
        if self.size == 0:
            raise IndexError("list index out of range")
        assert self.trailer.prev
        return self._delete(self.trailer.prev)

    def get_at(self, i: int) -> T:
        if i >= len(self):
            raise IndexError("list index out of range")
        assert self.head
        node = self.head.later_node(i)
        assert node.item is not None
        return node.item

    def set_at(self, i: int, x: T) -> None:
        if i >= len(self):
            raise IndexError("list index out of range")
        assert self.head
        node = self.head.later_node(i)
        node.item = x

    def insert_at(self, i: int, x: T) -> None:
        if i == 0:
            return self.insert_first(x)
        if i == len(self) - 1:
            return self.insert_last(x)
        if i > len(self):
            raise IndexError("list index out of range")
        assert self.head
        node = self.head.later_node(i - 1)
        assert node.next
        self._insert_between(x, node, node.next)

    def delete_at(self, i: int) -> T:
        if i == 0:
            return self.delete_first()
        if i == len(self) - 1:
            return self.delete_last()
        if i >= len(self):
            raise IndexError("list index out of range")
        assert self.head
        node = self.head.later_node(i - 1)
        assert node.next
        return self._delete(node.next)

    def _insert_between(
        self,
        x: T,
        predecessor: DoublyLinkedListNode[T],
        successor: DoublyLinkedListNode[T],
    ):
        new_node = DoublyLinkedListNode(x, next=successor, prev=predecessor)
        predecessor.next = new_node
        successor.prev = new_node
        self.size += 1

    def _delete(self, node: DoublyLinkedListNode[T]) -> T:
        assert node.next
        assert node.prev
        assert node.item is not None
        predecessor = node.prev
        successor = node.next
        predecessor.next = node.next
        successor.prev = node.prev
        self.size -= 1
        return node.item

    def _clear(self):
        while self.size > 0:
            self.delete_first()
