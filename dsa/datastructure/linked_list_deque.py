from typing import Generic, TypeVar
from dsa.datastructure.doubly_linked_list import DoublyLinkedList
from dsa.interface.deque import EmptyDequeException
from dsa.interface.deque import Deque


T = TypeVar("T")


class LinkedListDeque(Deque[T], Generic[T]):
    lst: DoublyLinkedList[T]

    def __init__(self) -> None:
        self.lst = DoublyLinkedList()

    def add_first(self, item: T) -> None:
        self.lst.insert_first(item)

    def add_last(self, item: T) -> None:
        self.lst.insert_last(item)

    def remove_first(self) -> T:
        try:
            return self.lst.delete_first()
        except IndexError:
            raise EmptyDequeException()

    def remove_last(self) -> T:
        try:
            return self.lst.delete_last()
        except IndexError:
            raise EmptyDequeException()

    def is_empty(self) -> bool:
        return len(self.lst) == 0
