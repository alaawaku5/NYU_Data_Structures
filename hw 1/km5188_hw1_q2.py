def shift(lst,k, dir = "left"):

    if dir == "left":
        temp = lst[:k]

        for i in lst[k:]:
            lst[lst.index(i)-k] = i
        lst[(len(lst)-k):] = temp
        return lst

    elif dir == "right":
        temp = lst[(len(lst)-k):]

        for i in lst[-k-1::-1]:
            lst[lst.index(i)+k] = i
        lst[:k] = temp
        return lst


