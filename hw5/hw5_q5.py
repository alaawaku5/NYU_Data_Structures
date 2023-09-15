from ArrayQueue import ArrayQueue
from ArrayStack import ArrayStack


def permutations(lst):
    lst_elements = ArrayStack()
    perms = ArrayQueue()
    for element in lst:
        lst_elements.push(element)
    temp = [lst_elements.pop()]
    perms.enqueue(temp)

    while not lst_elements.is_empty():
        val_to_insert = lst_elements.pop()

        for element in range(len(perms)):
            for position in range(len(perms.first()) + 1):
                first = perms.first().copy()
                first.insert(position, val_to_insert)
                perms.enqueue(first)
            perms.dequeue()

    res = []
    for i in range(len(perms)):
        res.append(perms.dequeue())
    return res

# print(permutations([1,2,3]))