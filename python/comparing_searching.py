"""
compire searching.
"""
from factory.searching import searching_factory

data = [x for x in range(1, 10001)]

target = 9225


searching = searching_factory.get_searching(
    algorithm="linear_search",
)

result = searching.search(
    data=data, target=target
)

searching = searching_factory.get_searching(
    algorithm="binary_search"
)

result = searching.search(
    data=data, target=target
)
