from typing import Type
import pytest
from dsa.datastructure.linked_list_deque import LinkedListDeque

from dsa.interface.deque import Deque, EmptyDequeException
from tests.helper.custom_type import FixtureRequest
from dsa.datastructure.circular_array_deque import CircularArrayDeque


class TestDeque:
    @pytest.fixture(params=[CircularArrayDeque[int], LinkedListDeque[int]])
    def implementation(self, request: FixtureRequest[Type[Deque[int]]]):
        return request.param

    @pytest.fixture
    def empty_dequeue(self, implementation: Type[Deque[int]]):
        return implementation()

    @pytest.fixture
    def dequeue_from_build(self, implementation: Type[Deque[int]]):
        built = implementation()
        built.build(x for x in range(5))
        return built

    def test_empty_dequeue(self, empty_dequeue: Deque[int]):
        assert empty_dequeue.is_empty()
        with pytest.raises(EmptyDequeException):
            empty_dequeue.remove_first()
        with pytest.raises(EmptyDequeException):
            empty_dequeue.remove_last()

    def test_basic_behavior(self, empty_dequeue: Deque[int]):
        empty_dequeue.add_first(10)
        empty_dequeue.add_last(20)
        empty_dequeue.add_first(5)
        just_add = empty_dequeue.remove_first()
        assert just_add == 5
        just_add = empty_dequeue.remove_last()
        assert just_add == 20

    def test_build(self, dequeue_from_build: Deque[int]):
        max_num = 5
        assert dequeue_from_build.remove_last() == max_num - 1
        dequeue_from_build.add_first(-1)
        assert dequeue_from_build.remove_first() == -1
        for i in range(0, (max_num - 1) // 2):
            assert dequeue_from_build.remove_first() == i
            assert dequeue_from_build.remove_last() == max_num - 2 - i

    def test_iter(self, dequeue_from_build: Deque[int]):
        for i, s in enumerate(dequeue_from_build):
            assert s == i
