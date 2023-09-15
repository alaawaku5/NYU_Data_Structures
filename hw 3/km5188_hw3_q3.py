def find_duplicates(lst):
    new = [""] * (len(lst) - 1)
    duplicates = []
    for i in lst:
        if new[i - 1] == "":
            new[i - 1] = 1
        elif new[i - 1] == 1:
            duplicates.append(i)
            new[i - 1] = 2

    return duplicates

