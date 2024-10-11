#!/usr/bin/env python3

"""
Description:
    This module add type annotations to the function
"""


from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default:
                     Union[T, None] = None) -> Union[Any, T]:
    """
    Parameters:
        dct: dictionary
        key: key

    Returns:
        any type
    """
    if key in dct:
        return dct[key]
    else:
        return default
