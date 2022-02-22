from typing import Type
import pytest

from dsa.datastructure.array_queue import ArrayQueue
from dsa.datastructure.linked_list_queue import LinkedListQueue
from dsa.interface.queue import Queue, EmptyQueueException
from tests.helper.custom_type import FixtureRequest


class TestQueue:
    @pytest.fixture(params=[ArrayQueue[int], LinkedListQueue[int]])
    def implementation(self, request: FixtureRequest[Type[Queue[int]]]):
        return request.param

    @pytest.fixture
    def empty_queue(self, implementation: Type[Queue[int]]):
        return implementation()

    @pytest.fixture
    def queue_from_build(self, implementation: Type[Queue[int]]):
        built = implementation()
        built.build(x for x in range(5))
        return built

    def test_empty_queue(self, empty_queue: Queue[int]):
        assert empty_queue.peek() is None
        assert empty_queue.is_empty()
        with pytest.raises(EmptyQueueException):
            empty_queue.dequeue()

    def test_basic_behavior(self, empty_queue: Queue[int]):
        empty_queue.enqueue(10)
        assert empty_queue.peek() == 10
        just_add = empty_queue.dequeue()
        assert just_add == 10

    def test_build(self, queue_from_build: Queue[int]):
        max_num = 5
        front = queue_from_build.peek()
        assert front == 0
        for i in range(4):
            t = queue_from_build.dequeue()
            assert t == i
        queue_from_build.enqueue(12)
        front = queue_from_build.dequeue()
        assert front == max_num - 1
        front = queue_from_build.peek()
        assert front == 12

    def test_iter(self, queue_from_build: Queue[int]):
        for i, s in enumerate(queue_from_build):
            assert s == i
