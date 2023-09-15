# q1
def is_palindrome(s):
    low = 0
    high = len(s) - 1
    while low < high:
        if s[low] != s[high]:
            return False
        low += 1
        high -= 1
    return True


str = "1racecar1"


# print(is_palindrome(str))


# q2
def reverse_vowels(input_str):
    lst = list(input_str)
    low = 0
    high = len(lst) - 1
    v1 = ""
    v2 = ""
    while low < high:
        if v1 != "" and v2 != "":
            lst[v1], lst[v2] = lst[v2], lst[v1]
            v1, v2 = "", ""

        if lst[low] in ['a', 'e', 'i', 'o', 'u'] and v1 == "":
            v1 = low
        if lst[high] in ['a', 'e', 'i', 'o', 'u'] and v2 == "":
            v2 = high
        low += 1
        high -= 1
    return "".join(lst)


# print(reverse_vowels("tandon"))


# q3a
def find_missing1(lst):
    s = 0
    e = len(lst) - 1

    while s <= e:
        m = (s + e) // 2
        if s == e:
            return s
        elif lst[m] == m:
            s = m + 1
        elif lst[m] > m:
            e = m


# q3b
def find_missing2(lst):
    n = len(lst)
    s1 = (n * (n + 1)) / 2
    s2 = 0
    for i in lst:
        s2 += i
    return int(s1 - s2)


lst = [8, 6, 0, 4, 3, 5, 1, 2]
print(find_missing2(lst))


# q4 part a
def find_pivot(lst):
    s = 0
    e = len(lst) - 1
    while s <= e:
        m = (s + e) // 2
        if s == e:
            return s
        elif lst[m] < lst[e]:
            e = m
        else:
            s = m + 1


# q4 part b
def shift_binary_search(lst, target):
    pivot = find_pivot(lst)
    if target <= lst[len(lst) - 1]:
        start = pivot
        end = len(lst) - 1
    else:
        end = pivot - 1
        start = 0

    while start <= end:
        mid = (start + end) // 2
        if lst[mid] == target:
            return mid
        elif target < lst[mid]:
            end = mid + 1
        elif target > lst[mid]:
            start = mid


lst = [15, 20, 21, 1, 3, 6, 7, 10, 12, 14]
print(find_pivot(lst))
print(shift_binary_search(lst, 12))
