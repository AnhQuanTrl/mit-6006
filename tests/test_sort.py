from typing import Type
import pytest

from dsa.algo.sorting import BubbleSort, SelectionSort, Sort
from tests.helper.custom_type import FixtureRequest


class TestSort:
    @pytest.fixture(params=[BubbleSort[int], SelectionSort[int]])
    def implementation(self, request: FixtureRequest[Type[Sort[int]]]):
        return request.param()

    def test_empty_list(self, implementation: Sort[int]):
        empty_list = []
        implementation.sort(empty_list)
        assert empty_list == []

    def test_one_element(self, implementation: Sort[int]):
        data = [1]
        implementation.sort(data)
        assert data == [1]

    def test_average_case(self, implementation: Sort[int]):
        data = [8, 4, 10, 2, 1, 99, 5]
        implementation.sort(data)
        assert data == [1, 2, 4, 5, 8, 10, 99]

    def test_monotonic_increasing(self, implementation: Sort[int]):
        data = [1, 2, 3, 4, 5, 6]
        implementation.sort(data)
        assert data == [1, 2, 3, 4, 5, 6]

    def test_monotonic_decreasing(self, implementation: Sort[int]):
        data = [6, 5, 4, 3, 2, 1]
        implementation.sort(data)
        assert data == [1, 2, 3, 4, 5, 6]
