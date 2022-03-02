from typing import Callable, Type
import pytest

from dsa.datastructure.position_list_impl import PositionalListImpl
from dsa.interface.positional_list import PositionalList
from tests.helper.custom_type import FixtureRequest


class TestPositionalList:
    @pytest.fixture(params=[PositionalListImpl[int]])
    def implementation(self, request: FixtureRequest[Type[PositionalList[int]]]):
        return request.param

    @pytest.fixture
    def empty_positional_list(self, implementation: Type[PositionalList[int]]):
        return implementation()

    @pytest.fixture
    def one_element_list(self, implementation: Type[PositionalList[int]]):
        def _one_element_list(e: int):
            lst = implementation()
            lst.add_first(e)
            return lst

        return _one_element_list

    def test_empty_list(self, empty_positional_list: PositionalList[int]):
        assert empty_positional_list.first() is None
        assert empty_positional_list.last() is None

    def test_add_one_element_1(self, empty_positional_list: PositionalList[int]):
        pos = empty_positional_list.add_first(5)
        assert pos.element == 5
        assert empty_positional_list.before(pos) is None
        assert empty_positional_list.after(pos) is None
        element = empty_positional_list.delete(pos)
        assert element == 5
        with pytest.raises(ValueError):
            empty_positional_list.add_after(pos, 10)

    def test_add_one_element_2(self, empty_positional_list: PositionalList[int]):
        pos = empty_positional_list.add_last(5)
        assert pos.element == 5
        assert empty_positional_list.before(pos) is None
        assert empty_positional_list.after(pos) is None
        element = empty_positional_list.delete(pos)
        assert element == 5
        with pytest.raises(ValueError):
            empty_positional_list.add_before(pos, 10)

    def test_position_of_different_container(
        self, one_element_list: Callable[[int], PositionalList[int]]
    ):
        lst1 = one_element_list(4)
        lst2 = one_element_list(10)
        pos = lst1.first()
        assert pos is not None and pos.element == 4
        with pytest.raises(ValueError):
            lst2.after(pos)

    def test_add_multiple_element(self, empty_positional_list: PositionalList[int]):
        pos1 = empty_positional_list.add_last(10)
        pos2 = empty_positional_list.add_first(5)
        pos3 = empty_positional_list.add_last(11)
        temp_pos = empty_positional_list.before(pos1)
        assert temp_pos == pos2
        temp_pos = empty_positional_list.after(pos1)
        assert temp_pos == pos3
        temp_pos = empty_positional_list.after(pos3)
        assert temp_pos is None
        temp_pos = empty_positional_list.before(pos3)
        assert temp_pos == pos1

    def test_add_multiple_element_then_delete(
        self, empty_positional_list: PositionalList[int]
    ):
        pos1 = empty_positional_list.add_last(10)
        pos2 = empty_positional_list.add_first(5)
        pos3 = empty_positional_list.add_last(11)
        val = empty_positional_list.delete(pos2)
        assert val == 5
        assert empty_positional_list.before(pos3) == pos1
        assert empty_positional_list.after(pos1) == pos3
        with pytest.raises(ValueError):
            empty_positional_list.before(pos2)
        with pytest.raises(ValueError):
            empty_positional_list.delete(pos2)
        val = empty_positional_list.delete(pos1)
        assert val == 10
        assert empty_positional_list.first() == empty_positional_list.last() == pos3

    def test_build_and_iter(self, empty_positional_list: PositionalList[int]):
        empty_positional_list.build(x for x in range(5))
        for x, i in zip(empty_positional_list, range(5)):
            assert x == i
