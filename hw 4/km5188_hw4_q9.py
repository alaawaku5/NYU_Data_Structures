def permutations(lst, low, high):
    if low == high:
        return [[lst[low]]]

    perm_list = []
    prev = permutations(lst, low+1, high)
    last = lst[low]

    for perm in prev:
        for i in range(len(perm)+1):
            new = perm[::]
            new.insert(i, last)
            perm_list.append(new)
    return perm_list

