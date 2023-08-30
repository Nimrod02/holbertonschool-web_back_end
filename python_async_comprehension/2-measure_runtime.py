#!/usr/bin/env python3
"""module 2 - measure_runtime
"""

import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """should measure the total
    runtime and return it.

    Returns:
        float: the measure of runtime
    """
    num_task = 4
    task = [async_comprehension() for _ in range(num_task)]

    start = asyncio.get_event_loop().time()

    await asyncio.gather(*task)

    total_runtime = asyncio.get_event_loop().time() - start
    return total_runtime
