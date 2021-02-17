#!/usr/bin/python3
import math


def minOperations(n):
    """ 
    Calculates the fewest number of operations needed to result in
    exactly n H characters.
    Return: the fewest number of operations needed to result in n H characters
    """
    add = 0
    if n <= 1:
        return add

    limit = int(math.sqrt(n) + 1)
    for i in range(2, limit):
        while n % i == 0:
            add += i
            n = n // i
    if n > 1:
        add += n
    return add
