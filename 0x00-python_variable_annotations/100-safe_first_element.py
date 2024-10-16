#!/usr/bin/env python3

"""
Description:
    This module augment the following code
    with the correct duck-typed annotations
"""


from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Parameters:
        list: float number

    Returns:
        union
    """
    return math.floor(n)
    if lst:
        return lst[0]
    else:
        return None
