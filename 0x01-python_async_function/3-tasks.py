#!/usr/bin/env python3

"""
Description:
    task_wait_random that takes an integer max_delay
    and returns an asyncio.Task
"""

import asyncio
from typing import Any

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Parameters:
        max_delay: int -> The maximum delay time

    Returns:
        asyncio.Task: An asyncio task that runs wait_random
    """
    task: asyncio.Task = asyncio.create_task(wait_random(max_delay))
    return task
