from typing import Generic, Optional, TypeVar

from .linked_list import LinkedList, LinkedListNode

T = TypeVar("T")


class TailLinkedList(LinkedList[T], Generic[T]):
    tail: Optional[LinkedListNode[T]]

    def __init__(self) -> None:
        super().__init__()
        self.tail = None

    def insert_first(self, x: T) -> None:
        super().insert_first(x)
        if len(self) == 1:
            self.tail = self.head

    def delete_first(self) -> T:
        x = super().delete_first()
        if self.head is None:
            self.tail = None
        return x

    def insert_last(self, x: T) -> None:
        if self.tail is None:
            self.insert_first(x)
            return
        node = LinkedListNode(x)
        self.tail.next = node
        self.tail = node
        self.size += 1

    def delete_last(self) -> T:
        if len(self) == 1:
            return self.delete_first()
        if len(self) == 0:
            raise IndexError("list index out of range")
        assert self.head is not None
        node = self.head.later_node(len(self) - 2)
        deleted_node = node.next
        assert deleted_node
        x = deleted_node.item
        node.next = deleted_node.next
        self.tail = node
        self.size -= 1
        return x

    def insert_at(self, i: int, x: T) -> None:
        if i == len(self):
            self.insert_last(x)
            return
        super().insert_at(i, x)

    def delete_at(self, i: int) -> T:
        if i == len(self) - 1:
            return self.delete_last()
        return super().delete_at(i)
