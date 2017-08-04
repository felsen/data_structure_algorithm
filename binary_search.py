"""
Binary search tree algorithm. recursive version.
"""


def binary_search(alist, item):
    first, last, found = 0, len(alist)-1, False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found


alist = [0, 1, 2, 8, 13, 17, 19, 32, 42, ]
print binary_search(alist, 3)
print binary_search(alist, 13)

