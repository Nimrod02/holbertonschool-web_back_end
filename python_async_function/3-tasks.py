#!/usr/bin/env python3
"""module 3- tasks
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay):
    """a function task_wait_random
    that takes an integer max_delay
    and returns a asyncio.Task.

    Args:
        max_delay (int): return the task
    """
    async def wrapper():
        result = await wait_random(max_delay)
        return result

    return asyncio.create_task(wrapper())
