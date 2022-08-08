#!/usr/bin/env python3

""" Function not asynchronous that returns a asyncrhonous task. """

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ Function not asynchronous that returns a asyncrhonous task. """
    return (asyncio.create_task(wait_random(max_delay)))
