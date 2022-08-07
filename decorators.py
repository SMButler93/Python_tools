"""A module containing custom decorators, adding further functionality to functions."""

import functools
import time


def repeats(num):
    """Repeats a function the specififed amount of times."""
    def repeat_dec(func):
        # Keeps the functions identifty.
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num):
                # loops for number of times specified in argument.
                function = func(*args, **kwargs)
            return function
        return wrapper
    return repeat_dec


def timer(func):
    """Times how long a function takes to run. Provides an output staing time taken"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # takes a time stamp before function is run.
        time_1 = time.time()
        function = func(*args, **kwargs)
        # Time stamp after function has ran.
        time_2 = time.time()
        # output data on taime taken for function to run.
        print(f"Time taken to run: {str(time_2 - time_1)[:6]}")
        return function
    return wrapper


def sleeper(seconds):
    """Sleeps/waits for the specified number of seconds before running."""
    def sleeper_dec(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Sleep/wait specified number of seconds before allowing function to run.
            time.sleep(seconds)
            return func(*args, **kwargs)
        return wrapper
    return sleeper_dec
