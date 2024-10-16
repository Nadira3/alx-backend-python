#!/usr/bin/env python3

"""
Description:
    Coroutine that collects 10 random numbers using an async comprehension
    over async_generator, then returns the 10 random numbers.
"""

import asyncio
from typing import List

# Import the async_generator from the other module
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Parameters: None

    Returns:
        list[float]: A list of 10 random float numbers.
    """
    random_numbers: list[float] = [num async for num in async_generator()]
    return random_numbers
