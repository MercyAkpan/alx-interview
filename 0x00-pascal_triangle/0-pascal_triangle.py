#!/usr/bin/python3
""" This module contains a function that returns a list of lists of integers
    representing the Pascal’s triangle of n"""


def pascal_triangle(n):
    """ This function returns a list of lists of integers
            representing the Pascal’s triangle of n
        Keyword arguments:
        n -- Ths is the number of rows of the triangle
        using the zero based index
        Return: A list of lists of integers representing
        the Pascal’s triangle of n
    """
    if n == 0:
        return []
    if n == 1:
        return [[1]]
    current = [1]
    history = pascal_triangle(n - 1)
    previous = history[-1]
    for i in range(n - 2):
        current.append(previous[i] + previous[i + 1])
    current.append(1)
    # print(history + [current])
    return (history + [current])
