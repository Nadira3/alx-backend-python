#!/usr/bin/env python3

"""
Description:
    This module takes a string k and an int
    OR float v as arguments and returns a tuple
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Parameters:
        k: string argument
        v: can either be int or float

    Returns:
        tuple: containing k and the square of v
    """
    return (k, v * v)
