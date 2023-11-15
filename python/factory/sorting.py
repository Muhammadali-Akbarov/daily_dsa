"""
sorting factory
"""
from abstract.sorting import Sorting

from algorithms.sorting.merge_sort import MergeSort
from algorithms.sorting.quick_sort import QuickSort
from algorithms.sorting.bubble_sort import BubbleSort
from algorithms.sorting.selection_sort import SelectionSort


class SortingFactory:
    """
    factory class for sorting classes
    """
    def get_sorting(self, algorithm: str) -> Sorting:
        """
        get sorting class for a given algorithm name.

        param: algorithm - name of the algorithm
        includes ("selection_sort", "bubble_sort", "merge_sort", "quick_sort")
        """
        sorting: Sorting = None

        if algorithm == "selection_sort":
            sorting = SelectionSort()

        if algorithm == "bubble_sort":
            sorting = BubbleSort()

        if algorithm == "merge_sort":
            sorting = MergeSort()

        if algorithm == "quick_sort":
            sorting = QuickSort()

        return sorting


sorting_factory = SortingFactory()
