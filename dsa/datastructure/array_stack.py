from typing import Generic, Optional, TypeVar
from dsa.datastructure.dynamic_array import DynamicArray

from dsa.interface.stack import Stack, StackUnderflowException


T = TypeVar("T")


class ArrayStack(Stack[T], Generic[T]):
    arr: DynamicArray[T]

    def __init__(self) -> None:
        self.arr = DynamicArray()

    def peek(self) -> Optional[T]:
        n = len(self.arr)
        return self.arr.get_at(n - 1) if n else None

    def pop(self) -> T:
        try:
            x = self.arr.delete_last()
        except IndexError:
            raise StackUnderflowException()
        return x

    def is_empty(self) -> bool:
        return len(self.arr) == 0

    def push(self, item: T) -> None:
        self.arr.insert_last(item)
