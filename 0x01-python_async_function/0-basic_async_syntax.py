#!/usr/bin/env python3

"""
Description:
    This module contains an asynchronous coroutine `wait_random`
    that takes an integer argument `max_delay`, waits for a random
    delay between 0 and `max_delay` seconds, and eventually returns
    the delay as a float.
"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous function that waits for a random delay.

    Args:
        max_delay (int): The maximum number of seconds to wait.
                         A random delay between 0 and `max_delay`
                         will be selected

    Returns:
        float: The random delay time.
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
