"""
The function help's to find the number by using sequentials search.
"""


def seq_search(item, find):
    found, pos = False, 0
    while pos < len(item) and not found:
        if item[pos] == find:
            found = True
        else:
            pos += 1
    return (found, pos)


print seq_search([12, 13, 14, 2, 3, 4, 5, 6, 7, 34, 34, 45, 56, ], 32)
print seq_search([1, 2, 3, 4, 5, 6, 7, 8, ], 5)
print seq_search([1, 2, 3, 4, 5, ], 100)
print seq_search([4, 5, 6, 7, ], 4)

