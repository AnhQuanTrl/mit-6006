from typing import Type
import pytest

from dsa.datastructure.array_stack import ArrayStack
from dsa.datastructure.linked_list_stack import LinkedListStack
from dsa.interface.stack import Stack, StackUnderflowException
from tests.helper.custom_type import FixtureRequest


class TestStack:
    @pytest.fixture(params=[ArrayStack[int], LinkedListStack[int]])
    def implementation(self, request: FixtureRequest[Type[Stack[int]]]):
        return request.param

    @pytest.fixture()
    def empty_stack(self, implementation: Type[Stack[int]]):
        return implementation()

    @pytest.fixture()
    def stack_from_build(self, implementation: Type[Stack[int]]):
        built = implementation()
        built.build(i for i in range(5))
        return built

    def test_empty_stack(self, empty_stack: Stack[int]):
        assert empty_stack.peek() is None
        assert empty_stack.is_empty()
        with pytest.raises(StackUnderflowException):
            empty_stack.pop()

    def test_push_and_pop(self, empty_stack: Stack[int]):
        empty_stack.push(10)
        just_add = empty_stack.pop()
        assert just_add == 10

    def test_build(self, stack_from_build: Stack[int]):
        max_num = 5
        top = stack_from_build.peek()
        assert top == max_num - 1
        for i in range(3):
            t = stack_from_build.pop()
            assert t == max_num - 1 - i
        top = stack_from_build.peek()
        assert top == max_num - 4

    def test_iter(self, stack_from_build: Stack[int]):
        max_num = 5
        for i, s in enumerate(stack_from_build):
            assert s == max_num - 1 - i
