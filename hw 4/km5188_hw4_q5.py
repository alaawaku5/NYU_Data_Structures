# q5a
def count_lowercase(s, low, high):
    if low > high:
        return 0
    if s[low].islower():
        return count_lowercase(s, low + 1, high) + 1
    else:
        return count_lowercase(s, low + 1, high)


# q5b
def is_number_of_lowercase_even(s, low, high):
    if low > high:
        return True
    else:
        if s[low].islower():
            return not is_number_of_lowercase_even(s, low + 1, high)
        else:
            return is_number_of_lowercase_even(s, low + 1, high)
