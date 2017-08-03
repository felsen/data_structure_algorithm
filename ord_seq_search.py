"""
This is the function is for search element by order.
"""


def ord_seq_search(item_list, item):
    found, stop, pos = False, False, 0
    while pos < len(item_list) and not found and not stop:
        if item_list[pos] == item:
            found = True
        else:
            if item_list[pos] > item:
                stop = True
            else:
                pos += 1
    return found


l = [0, 1, 2, 8, 13, 17, 19, 32, 42, ]
print ord_seq_search(l, 3)
print ord_seq_search(l, 13)
