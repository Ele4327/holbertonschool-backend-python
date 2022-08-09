#!/usr/bin/env python3

"""
A coroutine will collect 10 random numbers using an async comprehensing,
then return the 10 random numbers.
"""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """Collect numbers using an async comprehensing over async_generator"""
    total = [x async for x in async_generator]
    return(total)
