#!/usr/bin/env python3
"""module 1 - concurrent_coroutines
"""


import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """n async routine called wait_n
    that takes in 2 int arguments (in this order):
    n and max_delay.
    You will spawn wait_random n times with the specified max_delay.

    Args:
        n (int): number of routine
        max_delay (int): max delay for tasks

    Returns:
        delay: return in seconds the delay for each task
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
