#!/usr/bin/python3
"""finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""
    tmp = list_of_integers
    i = len(tmp)
    if i == 0:
        return
    m = i // 2
    if (m == i - 1 or tmp[m] >= tmp[m + 1]) and (m == 0 or tmp[m] >= tmp[m - 1]):
        return li[m]
    if m != i - 1 and tmp[m + 1] > tmp[m]:
        return find_peak(tmp[m + 1:])
    return find_peak(tmp[:m])
