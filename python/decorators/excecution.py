"""
calculates time execution.
"""
import time
import functools

import colorama

colorama.init(autoreset=True)


def time_execution(func):
    """
    time execution decorator
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not hasattr(wrapper, 'is_recursive'):
            wrapper.is_recursive = True
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            wrapper.is_recursive = False
            # pylint: disable=line-too-long
            result = f"Total execution time of class name: {func.__str__()} method: {func.__name__} time: {end_time - start_time} seconds" # noqa
            print(colorama.Fore.GREEN + result)

        else:
            result = func(*args, **kwargs)
        return result

    return wrapper
