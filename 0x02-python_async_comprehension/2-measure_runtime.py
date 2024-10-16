#!/usr/bin/env python3


"""
Description:
    coroutine will collect 10 random numbers using an async comprehensing
    over async_generator, then return the 10 random numbers
"""


import random
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Parameters: None

    Returns:
        float
    """
    tasks = [
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            async_comprehension()
    ]
    s = time.perf_counter()
    await asyncio.gather(*tasks)
    elapsed_time = time.perf_counter() - s
    return elapsed_time
