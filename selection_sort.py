"""
Selection sort.
"""


def selection_sort(alist):
    for fillslot in xrange(len(alist)-1, 0, -1):
        position_of_max = 0
        for location in xrange(1, fillslot+1):
            if alist[location] > alist[position_of_max]:
                position_of_max = location
        temp = alist[fillslot]
        alist[fillslot] = alist[position_of_max]
        alist[position_of_max] = temp


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20, ]
selection_sort(alist)
print alist

