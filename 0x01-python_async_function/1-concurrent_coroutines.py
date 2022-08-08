#!/usr/bin/env python3

"""Function async that executes multiples coroutines concurrently"""

from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """First executes multiple coroutines concurrently
    and then returns all the values in a list, and then
    organize that values in ascending order without sort"""
    list_value = []
    for z in range(n):
        i = await wait_random(max_delay)
        list_value.append(i)

    new_list = []
    while list_value:
        min = list_value[0]
        for x in list_value:
            if x < min:
                min = x
        new_list.append(min)
        list_value.remove(min)

    return (new_list)
