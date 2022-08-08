#!/usr/bin/env python3

"""
    Function asynchronous that waits a random number of seconds
    between 0 and max_delay.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Function asynchronous that waits a random number of seconds
    between 0 and max_delay."""
    x = random.uniform(0, max_delay)
    await asyncio.sleep(x)

    return x
