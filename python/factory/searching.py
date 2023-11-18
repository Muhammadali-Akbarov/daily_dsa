"""
searching factory
"""
from abstract.searching import Searching


from algorithms.searching.linear import LinearSearch
from algorithms.searching.binary import BinarySearch


class SearchingFactory:
    """
    factory class for searching classes
    """
    def get_searching(self, algorithm: str) -> Searching:
        """
        get searching class for a given algorithm name.

        param: algorithm - name of the algorithm
        includes ("linear_search", binary_search)
        """
        searching: Searching = None

        if algorithm == "linear_search":
            searching = LinearSearch()

        if algorithm == "binary_search":
            searching = BinarySearch()

        return searching


searching_factory = SearchingFactory()
