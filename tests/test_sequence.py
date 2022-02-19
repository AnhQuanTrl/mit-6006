from typing import Type
import pytest
from dsa.datastructure.dynamic_array import DynamicArray
from dsa.datastructure.linked_list import LinkedList
from dsa.datastructure.static_array import StaticArray
from dsa.interface.sequence import Sequence
from tests.helper.custom_type import FixtureRequest


class TestSequence:
    @pytest.fixture(params=[StaticArray[int], LinkedList[int], DynamicArray[int]])
    def implementation(self, request: FixtureRequest[Type[Sequence[int]]]):
        return request.param

    @pytest.fixture()
    def empty_sequence(self, implementation: Type[Sequence[int]]):
        return implementation()

    @pytest.fixture()
    def sequence_from_build(self, implementation: Type[Sequence[int]]):
        arr = implementation()
        arr.build(x for x in range(10))
        return arr

    def test_empty_sequence(self, empty_sequence: Sequence[int]):
        assert len(empty_sequence) == 0
        with pytest.raises(IndexError):
            empty_sequence.get_at(0)

    def test_sequence_basic_operations(self, empty_sequence: Sequence[int]):
        empty_sequence.insert_first(10)
        empty_sequence.set_at(0, 15)
        x = empty_sequence.delete_last()
        assert x == 15
        for i in range(3):
            empty_sequence.insert_at(i, i)
        middle = empty_sequence.get_at(1)
        assert middle == 1
        deleted = empty_sequence.delete_at(0)
        assert deleted == 0
        assert len(empty_sequence) == 2
        for i in range(2):
            assert empty_sequence.get_at(i) == i + 1

    def test_build(self, sequence_from_build: Sequence[int]):
        for i in range(10):
            assert sequence_from_build.get_at(i) == i

    def test_iter(self, sequence_from_build: Sequence[int]):
        for i, j in zip(sequence_from_build, (a for a in range(10))):
            assert i == j

    def test_random_access(self, sequence_from_build: Sequence[int]):
        assert sequence_from_build.get_at(5) == 5
        assert sequence_from_build.get_at(9) == 9
        sequence_from_build.set_at(9, 20)
        assert sequence_from_build.get_at(9) == 20
        with pytest.raises(IndexError):
            sequence_from_build.set_at(10, 30)
