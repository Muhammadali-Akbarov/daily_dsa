"""
compiring
"""
import random

from factory.sorting import sorting_factory


# create shuffled array
data = [random.randint(1, 1000) for _ in range(15000)]


sorting = sorting_factory.get_sorting(
    algorithm="quick_sort",
)

sorting.sort(
    data=data
)

sorting = sorting_factory.get_sorting(
    algorithm="merge_sort",
)

sorting.sort(
    data=data
)

sorting = sorting_factory.get_sorting(
    algorithm="selection_sort",
)

sorting.sort(
    data=data
)

sorting = sorting_factory.get_sorting(
    algorithm="bubble_sort",
)

sorting.sort(
    data=data
)
