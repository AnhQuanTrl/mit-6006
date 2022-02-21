from typing import Generic, Optional, TypeVar
from dsa.datastructure.linked_list import LinkedList

from dsa.interface.stack import Stack, StackUnderflowException


T = TypeVar("T")


class LinkedListStack(Stack[T], Generic[T]):
    lst: LinkedList[T]

    def __init__(self) -> None:
        self.lst = LinkedList()

    def is_empty(self) -> bool:
        return len(self.lst) == 0

    def push(self, item: T) -> None:
        self.lst.insert_first(item)

    def pop(self) -> T:
        try:
            x = self.lst.delete_first()
        except IndexError:
            raise StackUnderflowException
        return x

    def peek(self) -> Optional[T]:
        return self.lst.get_at(0) if not self.is_empty() else None
