def list_min(lst, low, high):
    if low == high:
        return lst[low]
    elif list_min(lst, low + 1, high) < lst[low]:
        return list_min(lst, low + 1, high)
    return lst[low]


a = []
print(list_min(a, 0, 0))
