s = "ashock"

a = []


def unique_chars():
    success = True
    for i in s:
        if i not in a:
            a.append(i)
        else:
            success = False
            break
    return success


print unique_chars()
