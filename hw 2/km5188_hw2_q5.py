def split_parity(lst):
    left = 0
    right = len(lst) - 1
    low, high = "", ""
    while left < right:
        if low != "" and high != "":
            lst[low], lst[high] = lst[high], lst[low]
            left += 1
            right -= 1
            low, high = "", ""
        if lst[left] % 2 == 0:
            low = left
        else:
            left += 1
        if lst[right] % 2 == 1:
            high = right
        else:
            right -= 1

