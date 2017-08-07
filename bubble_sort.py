"""
Bubble sort.
"""


def bubble_sort(alist):
    for num in xrange(len(alist)-1, 0, -1):
        for n in xrange(num):
            if alist[n] > alist[n+1]:
                temp = alist[n]
                alist[n] = alist[n+1]
                alist[n+1] = temp
    return alist


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20, ]
print bubble_sort(alist)


def bubble_sort_n(alist):
    for i in range(len(alist)):
        for j in range(i):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
    return alist


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20, ]
print bubble_sort_n(alist)

