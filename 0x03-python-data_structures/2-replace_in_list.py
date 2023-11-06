#!/usr/bin/python3
# prints all integers of a list, in reverse order.


def replace_in_list(my_list, idx, element):
    if idx >= 0 and idx < len(my_list):
        my_list[idx] = element
    return (my_list)
