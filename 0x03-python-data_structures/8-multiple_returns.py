#!/usr/bin/python3


def multiple_returns(sentence):
    """returns tuple length of a string and it first character"""
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
