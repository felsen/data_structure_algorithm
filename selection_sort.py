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


def selection_sort_max(alist):
    """
    Still some issue was in this function.
    """
    position_element = None
    for j in xrange(len(alist) + 1):
        for i in xrange(j+1):
            if len(alist[:position_element]):
                element_max = max(alist[:position_element])
                position_idx = alist.index(element_max)
                if position_element is None:
                    position_element = -1
                    alist[position_idx], \
                        alist[position_element] \
                        = alist[position_element], alist[position_idx]
                position_element -= 1
    return alist


alist = [10, 2, 4, 9, 6, 5, 7, 12, 3, 1]
alist = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11]
alist = [54, 26, 93, 17, 77, 31, 44, 55, 20, ]
print selection_sort_max(alist)

