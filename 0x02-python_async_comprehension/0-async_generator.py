#!/usr/bin/env python3
"""Coroutine async, create generator that loops 10 times
    and wait 1 second, then yield a random number
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Loop 10 times, await 1 sec for each time and
    yield a random number float between 0 and 10"""
    for x in range(10):
        await asyncio.sleep(1)
        yield(random.uniform(0, 10))
