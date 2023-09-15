def split_by_sign(lst, low, high):
    if low >= high:
        return lst
    elif low <= high:
        if lst[low] > 0 and lst[high] < 0:
            lst[low], lst[high] = lst[high], lst[low]
        if lst[low] < 0:
            low += 1
        if lst[high] > 0:
            high -= 1
        split_by_sign(lst, low, high)


