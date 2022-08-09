#!/usr/bin/env python3

"""Measure the total runtime and return it. After being executed
another coroutine four times in pararell using gather, the total runtime"""

import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure the runtime of an async comprehension, and return it"""
    start = time.time()
    await asyncio.gather(*(async_comprehension() for x in range(4)))
    end = time.time()
    return(end - start)
