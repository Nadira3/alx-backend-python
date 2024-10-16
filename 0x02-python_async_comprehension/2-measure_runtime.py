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
        float: The elapsed time in seconds for running
        async_comprehension four times.
    """
    tasks: list[Coroutine[Any, Any, list[float]]] = [
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    ]

    s: float = time.perf_counter()
    await asyncio.gather(*tasks)
    elapsed_time: float = time.perf_counter() - s
    return elapsed_time
