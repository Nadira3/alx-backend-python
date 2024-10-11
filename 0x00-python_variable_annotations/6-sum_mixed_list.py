#!/usr/bin/env python3

"""
Description:
    This module returns a mixed list
"""


from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    Parameters:
        mxd_list: The list of mixed int and floating point numbers

    Returns:
        float: sum of list elements
    """
    return sum(mxd_list)
