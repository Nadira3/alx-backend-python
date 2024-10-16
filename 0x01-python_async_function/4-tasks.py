#!/usr/bin/env python3

"""
Description:
    async routine called wait_n that takes in 2 int arguments
"""


import random
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Parameters:
        n: int -> number of spawn times
        max_delay: delay time

    Returns:
        list
    """
    wait_tasks = [task_wait_random(max_delay) for _ in range(n)]

    sorted_delays: List[float] = []  # Initialize the list for sorted results

    # Wait for each task to complete
    for task in asyncio.as_completed(wait_tasks):
        delay = await task  # Get the completed delay
        # Insert the delay in sorted order
        inserted = False
        for i in range(len(sorted_delays)):
            if delay < sorted_delays[i]:
                sorted_delays.insert(i, delay)
                inserted = True
                break
        if not inserted:
            sorted_delays.append(delay)  # Append to the end if not inserted

    return sorted_delays
