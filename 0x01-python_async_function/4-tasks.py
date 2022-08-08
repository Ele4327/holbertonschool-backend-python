#!/usr/bin/env python3

"""
    Function async that executes multiples coroutines concurrently
    and wait a randomly amount of time between 0 and max_delay
"""

from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """First executes multiple coroutines concurrently
    and wait a randomly amount of time between 0 and max_delay
    and then returns all the values in a list, and then
    organize that values in ascending order without sort"""
    list_value = []
    for z in range(n):
        i = await task_wait_random(max_delay)
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
