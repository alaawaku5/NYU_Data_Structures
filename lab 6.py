# 1
def sum_to(n):
    if n == 0:
        return 0
    return n + sum_to(n - 1)


# print(sum_to(4))


# 2
def product_evens(n):
    if n == 2:
        return 2
    return n * product_evens(n - 2)


# print(product_evens(8))


# 3
def find_max(lst, l, h):
    if l == h:
        return lst[l]
    prev = find_max(lst, l + 1, h)
    if prev > lst[l]:
        return prev
    return lst[l]


# print(find_max([13, 9, 16, 30, 4, 2], 0, 5))


# 4

def is_palindrome(str1, low, high):
    str = list(str1)
    while low <= high:
        if str[low] != str[high]:
            return False

        if (low == high and str[low] == str[high]) or (low + 1 == high and str[low] == str[high]):
            return True

        if str[low] == str[high]:
            low = + 1
            high = + 1


# print(is_palindrome('race car',0,6))

# 5 binary search recursively

def binary_search(lst, low, high, val):
    if low <= high:
        mid = (low + high) // 2
        if lst[mid] == val:
            return mid
        elif val > lst[mid]:
            return binary_search(lst, mid + 1, high, val)
        elif val < lst[mid]:
            return binary_search(lst, low, mid, val)


lst = [1, 2, 3, 4, 5, 5]
print("nn", binary_search(lst, 0, 5, 3))


def merge_sort(lst):
    if len(lst) == 0:
        return lst
    elif len(lst) == 1:
        return lst
    else:
        mid = (0 + len(lst) - 1) // 2
        lst1 = lst[:mid + 1]
        lst2 = lst[mid + 1:]
        merge_sort(lst1)
        merge_sort(lst2)
        merged = merge(lst1, lst2)
        lst[:] = merged[:]


def merge(lst1, lst2):
    merged_lst = []
    i1 = 0
    i2 = 0
    while i1 < len(lst1) and i2 < len(lst2):
        if lst1[i1] < lst2[i2]:
            merged_lst.append(lst1[i1])
            i1 += 1
        else:
            merged_lst.append(lst2[i2])
            i2 += 1
    while i1 < len(lst1):
        merged_lst.append(lst1[i1])
        i1 += 1
    while i2 < len(lst2):
        merged_lst.append(lst2[i2])
        i2 += 1
    return merged_lst


lst = [38, 27, 43, 3, 9, 81, 10, 1]
merge_sort(lst)
print(lst)


# 6 vowel and consonant count
def vc_count(word, low, high):
    if low <= high:
        if low == high:
            if word[low] in ['a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U']:
                return 1, 0
            else:
                return 0, 1

    v, c = vc_count(word, low + 1, high)
    print(v,c)
    if word[low] in ['a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U']:
        v += 1
    else:
        c += 1
    return v, c


word = "NYUTandonEngineering"
print(vc_count(word, 0, 19))

def binary_search(lst,low,high):
    if low<=high:
