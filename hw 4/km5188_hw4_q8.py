def flat_list(lst, low, high):
    if low > high:
        return []
    new = []
    for i in range(low, high + 1):
        if isinstance(lst[i], int):
            new.append(lst[i])
        elif isinstance(lst[i], list):
            x = flat_list(lst[i], 0, len(lst[i]) - 1)
            new.extend(x)
    return new


a = [[1, 2], 3, [4, [5, 6, [7], 8]]]
b = []
print(flat_list(b, 0, 0))


#    required method
def flat_list(nested_lst, low, high):
    if low > high:
        return []
    flattened = []
    if type(nested_lst[low]) == list:
        flattened += flat_list(nested_lst[low], 0, len(nested_lst[low]) - 1)
    else:
        flattened.append(nested_lst[low])
        flattened += flat_list(nested_lst, low + 1, high)

    return flattened


n = [[1, 2], 3, [4, [5, 6, [7], 8]]]
# print(flat_list(nested_lst, 0, 2))
