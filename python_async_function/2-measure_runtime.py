#!/usr/bin/env python3
"""module 2 - measure_runtime
"""


import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n, max_delay):
    """ a measure_time function
    with integers n and max_delay as arguments
    that measures the total execution time for wait_n(n, max_delay),
    and returns total_time / n. Your function should return a float.

    Args:
        n (int): arguments that measures the total execution
        max_delay (int): arguments that measures the total execution

    Returns:
        float: total time of execution
    """
    total_time = 0

    for _ in range(n):
        start_time = time.time()
        wait_n(n, max_delay)
        end_time = time.time()

        total_time += (end_time - start_time)

    average_time = total_time / n

    return average_time


if __name__ == "__main__":
    n = 10
    max_delay = 2

    loop = asyncio.get_event_loop()
    avg_execution_time = loop.run_until_complete(measure_time(n, max_delay))
    loop.close()
