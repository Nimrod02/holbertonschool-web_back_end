#!/usr/bin/env python3
"""
module 4 - tasks
"""


import asyncio
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
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
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
