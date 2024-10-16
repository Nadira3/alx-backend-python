#!/usr/bin/env python3

"""
Description:
    Coroutine that loops 10 times, each time asynchronously waits 1 second,
    then yields a random number between 0 and 10.
"""

import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Coroutine that yields a random float between 0 and 10
    after a 1-second delay.

    Returns:
        Generator[float, None, None]: Yields a float value between 0 and 10.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
