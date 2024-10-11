#!/usr/bin/env python3

"""
Description:
    This module takes a float multiplier as argument
    and returns a function that multiplies a float by multiplier
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Parameters:
        multiplier: The number argument as a float

    Returns:
        function: multiplier function
    """
    return lambda x: x * multiplier
