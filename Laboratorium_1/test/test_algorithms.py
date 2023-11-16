from Laboratorium_1.algorithms import Algorithms


class TestAlgorithms:
    def test_minimum_empty(self):
        assert Algorithms.minimum([]) is None

    def test_minimum_single_element(self):
        assert Algorithms.minimum([5]) == 5

    def test_minimum_multiple_elements(self):
        assert Algorithms.minimum([3, 1, 2]) == 1

    def test_minimum_repeating_elements(self):
        assert Algorithms.minimum([2, 2, 2]) == 2

    def test_minimum_negative_elements(self):
        assert Algorithms.minimum([-1, -3, -2]) == -3

    def test_maximum_empty(self):
        assert Algorithms.maximum([]) is None

    def test_maximum_single_element(self):
        assert Algorithms.maximum([5]) == 5

    def test_maximum_multiple_elements(self):
        assert Algorithms.maximum([1, 3, 2]) == 3

    def test_maximum_mixed_elements(self):
        assert Algorithms.maximum([-1, 3, 2]) == 3

    def test_bubble_sort_normal(self):
        assert Algorithms.bubble_sort([3, 2, 1]) == [1, 2, 3]

    def test_bubble_sort_empty(self):
        assert Algorithms.bubble_sort([]) == []

    def test_bubble_sort_repeating_elements(self):
        assert Algorithms.bubble_sort([3, 1, 3, 2]) == [1, 2, 3, 3]

    def test_bubble_sort_negative_elements(self):
        assert Algorithms.bubble_sort([-3, -1, -2]) == [-3, -2, -1]

    def test_bubble_sort_already_sorted(self):
        assert Algorithms.bubble_sort([1, 2, 3]) == [1, 2, 3]

    def test_bubble_sort_performance(self):
        large_list = list(range(1000, 0, -1))
        sorted_list = Algorithms.bubble_sort(large_list)
        assert sorted_list == list(range(1, 1001))
