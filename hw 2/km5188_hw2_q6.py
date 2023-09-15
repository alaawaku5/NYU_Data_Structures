def two_sum(srt_lst, target):
    low = 0
    high = len(srt_lst) - 1
    while low < high:
        if srt_lst[high] + srt_lst[low] == target:
            return low, high
        elif target - srt_lst[high] > srt_lst[low]:
            low += 1
        elif target - srt_lst[high] < srt_lst[low]:
            high -= 1



