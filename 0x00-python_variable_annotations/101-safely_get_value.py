#!/usr/bin/env python3

"""
Description:
    This module add type annotations to the function
"""


from typing import TypeVar, Mapping, Any, Union

type NoneType = None
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default:
    """
    Parameters:
        dct: dictionary
        key: key

    Returns:
        any type
    """
                     Union[T, NoneType] = None) -> Union[Any, T]:
    if key in dct:
        return dct[key]
    else:
        return default
