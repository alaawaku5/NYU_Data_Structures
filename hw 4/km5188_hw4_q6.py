def appearances(s, low, high):
    if low > high:
        return {}
    rest_dict = appearances(s, low + 1, high)
    if s[low] in rest_dict:
        rest_dict[s[low]] += 1
    else:
        rest_dict[s[low]] = 1
    return rest_dict

