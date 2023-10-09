#!/usr/bin/env python3
"""
function sum_mixed_list which takes a list mxd_lst
of integers and floats and returns their sum as a float.
"""


def sum_mixed_list(mxd_lst: list[int | str]) -> float:
    """
    sums up list content
    """
    return sum(mxd_lst)
