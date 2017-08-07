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


def bubble_sort_m(alist):
    exchange = True
    passnum = len(alist) - 1
    while passnum > 0 and exchange:
        exchange = False
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
        passnum -= 1


alist = [20, 30, 40, 90, 50, 60, 70, 80, 100, 110, ]
bubble_sort_m(alist)
print alist


