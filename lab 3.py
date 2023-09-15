# lab 3 a and b
def reverse_list(lst, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(lst) - 1
    while low <= high:
        lst[low], lst[high] = lst[high], lst[low]
        low += 1
        high -= 1
    return lst


lst = [1, 32, 4, 56, 7]
print(reverse_list(lst, 1, 3))


# lab 3 question 2
def move_zeros(nums):
    s = ""
    for i in range(len(nums)):
        if s == "" and nums[i] == 0:
            s = i
        if nums[i] != 0 and s != "":
            nums[i], nums[s] = nums[s], nums[i]
            if nums[s + 1] == 0:
                s = s + 1
            elif nums[i] != 0:
                s = i
    return nums


nums = [0, 1, 0, 0, 0, 3, 13, 0]
print(move_zeros(nums))


# lab 3 question 3
def shift(lst, k):
    reverse_list(lst)
    reverse_list(lst, 0, k - 1)
    reverse_list(lst, k, len(lst) - 1)
    return lst


lst = [1, 2, 3, 4, 5, 6]
print(shift(lst, 2))


# lab 3 question 4
def max_sum(nums, k):
    # initialization
    curr = 0
    for i in range(0, len(nums) // k):
        curr += nums[i]
    left = 1
    right = left + len(nums) // k - 1
    max = curr

    while right < len(nums):
        curr = curr - nums[left-1] + nums[right]
        if max < curr:
            max = curr
        left += 1
        right += 1
    return max


nums = [1, 4, 2, 10, 23, 3, 1, 0, 20]
print(max_sum(nums, 2))
