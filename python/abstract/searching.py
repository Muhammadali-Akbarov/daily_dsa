"""
abstract class for searching
"""
import abc
import typing


class Searching(abc.ABC):
    """
    abstract class for searching.
    """
    @abc.abstractmethod
    def search(self, data: typing.List, target: int) -> typing.Union[int, None]:
        """
        implement the search method.
        """
        raise NotImplementedError("implement searching method in subclass")
