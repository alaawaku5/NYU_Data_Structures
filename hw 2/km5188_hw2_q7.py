def findChange(lst01):
    start = 0
    end = len(lst01) - 1

    while start < end:
        mid = (start + end) // 2
        if lst01[mid] == 0 and lst01[mid + 1] == 1:
            return mid + 1

        if lst01[mid] == 1 and lst01[mid + 1] == 1:
            end = mid

        if lst01[mid] == 0 and lst01[mid + 1] == 0:
            start = mid + 1


