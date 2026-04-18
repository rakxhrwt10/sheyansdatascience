'''

Remove Duplicates Using Set



Write a Python program to remove duplicate elements from a list
using a set. The program should take a list of integers as input And 
output a list containing only unique elements.

'''



def remove_duplicates_using_set(n, elements):
    seen = set()
    result = []

    for i in elements:
        if i not in seen:
            seen.add(i)
            result.append(i)

    return result 

