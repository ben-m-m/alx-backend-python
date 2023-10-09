#!/usr/bin/env python3
"""
Annotate the below function’s parameters and
return values with the appropriate types
"""
from typing import Tuple, Sequence, List, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    return a list of tuples with the element and its
    length in it
    """
    return [(i, len(i)) for i in lst]
