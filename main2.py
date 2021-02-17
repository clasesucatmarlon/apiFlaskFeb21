#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('min').minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 9
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 6
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))