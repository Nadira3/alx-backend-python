#!/usr/bin/env python3

"""
Description:
    This module annotate the below function’s parameters and
    return values with the appropriate types
"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Parameters:
        lst: an iterable containing a sequence

    Returns:
        list: of tuple and int
    """
    return [(i, len(i)) for i in lst]
