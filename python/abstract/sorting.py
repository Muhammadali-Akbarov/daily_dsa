"""
abstract class for sorting
"""
import abc
import typing


class Sorting(abc.ABC):
    """
    abstract class for sorting.
    """
    @abc.abstractmethod
    def sort(self, data: typing.List) -> typing.Union[typing.List, None]:
        """
        sorts the data in-place and returns the sorted data.
        """
        raise NotImplementedError("implement sort method in subclass")
