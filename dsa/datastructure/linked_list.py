from __future__ import annotations
from typing import Generic, Optional, TypeVar
from collections.abc import Iterator, Iterable

from dsa.interface.sequence import Sequence

T = TypeVar("T")


class LinkedListNode(Generic[T]):
    item: T
    next: Optional[LinkedListNode[T]]

    def __init__(self, x: T, next: Optional[LinkedListNode[T]] = None):
        self.item = x
        self.next = next

    def later_node(self, i: int) -> LinkedListNode[T]:
        if i == 0:
            return self
        assert self.next
        return self.next.later_node(i - 1)


class LinkedList(Sequence[T], Generic[T]):
    head: Optional[LinkedListNode[T]]
    size: int

    def __init__(self) -> None:
        self.head = None
        self.size = 0

    def __len__(self) -> int:
        return self.size

    def __iter__(self) -> Iterator[T]:
        node = self.head
        while node:
            yield node.item
            node = node.next

    def build(self, X: Iterable[T]) -> None:
        current_node: Optional[LinkedListNode[T]] = None
        for x in X:
            if not current_node:
                current_node = LinkedListNode(x)
                self.head = current_node
            else:
                current_node.next = LinkedListNode(x)
                current_node = current_node.next
            self.size += 1

    def get_at(self, i: int) -> T:
        if i >= len(self):
            raise IndexError("list index out of range")
        assert self.head
        node = self.head.later_node(i)
        return node.item

    def set_at(self, i: int, x: T) -> None:
        if i >= len(self):
            raise IndexError("list index out of range")
        assert self.head
        node = self.head.later_node(i)
        node.item = x

    def insert_first(self, x: T) -> None:
        node = LinkedListNode(x, self.head)
        node.next = self.head
        self.head = node
        self.size += 1

    def delete_first(self) -> T:
        if not self.head:
            raise IndexError("list index out of range")
        x = self.head.item
        self.head = self.head.next
        self.size -= 1
        return x

    def insert_at(self, i: int, x: T) -> None:
        if i == 0:
            return self.insert_first(x)
        if i > len(self):
            raise IndexError("list index out of range")
        assert self.head
        node = self.head.later_node(i - 1)
        new_node = LinkedListNode(x, node.next)
        node.next = new_node
        self.size += 1

    def delete_at(self, i: int) -> T:
        if i == 0:
            return self.delete_first()
        if i >= len(self):
            raise IndexError("list index out of range")
        assert self.head
        node = self.head.later_node(i - 1)
        deleted_node = node.next
        assert deleted_node
        x = deleted_node.item
        node.next = deleted_node.next
        self.size -= 1
        return x

    def insert_last(self, x: T) -> None:
        return self.insert_at(len(self), x)

    def delete_last(self) -> T:
        return self.delete_at(len(self) - 1)
