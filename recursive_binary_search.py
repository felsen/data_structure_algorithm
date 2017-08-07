"""
Recursive binary search ...
"""


def rec_binary_search(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                return rec_binary_search(alist[:midpoint], item)
            else:
                return rec_binary_search(alist[midpoint+1:], item)


alist = [0, 1, 2, 8, 13, 17, 19, 32, 42, ]
print rec_binary_search(alist, 3)
print rec_binary_search(alist, 13)

