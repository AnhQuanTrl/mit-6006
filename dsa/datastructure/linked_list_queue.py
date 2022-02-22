from typing import Generic, Optional, TypeVar
from dsa.datastructure.tail_linked_list import TailLinkedList

from dsa.interface.queue import EmptyQueueException, Queue


T = TypeVar("T")


class LinkedListQueue(Queue[T], Generic[T]):
    lst: TailLinkedList[T]

    def __init__(self) -> None:
        self.lst = TailLinkedList()

    def peek(self) -> Optional[T]:
        try:
            x = self.lst.get_at(0)
        except IndexError:
            x = None
        return x

    def enqueue(self, item: T) -> None:
        self.lst.insert_last(item)

    def dequeue(self) -> T:
        try:
            x = self.lst.delete_first()
        except IndexError:
            raise EmptyQueueException()
        return x

    def is_empty(self) -> bool:
        return len(self.lst) == 0
