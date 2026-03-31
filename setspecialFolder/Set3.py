'''

Symmetric Difference Finder
Medium

Description
Write a Python program to find the symmetric difference
between two sets. The symmetric difference contains elements
that are in either of the sets but not in both.

'''


def symmetric_difference_finder(n, set1, m, set2):
    # Write your code here
    a=set(set1)
    b=set(set2)
    return a.symmetric_difference(b)