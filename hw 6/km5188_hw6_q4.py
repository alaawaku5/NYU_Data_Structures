from DoublyLinkedList import DoublyLinkedList


def copy_linked_list(lnk_lst):
    lst_copy = DoublyLinkedList()
    p2 = lnk_lst.header.next
    for i in range(len(lnk_lst)):
        lst_copy.add_last(p2.data)
        p2 = p2.next
    return lst_copy


def deep_copy_linked_list(lnk_lst):
    lst_copy = DoublyLinkedList()
    pointer = lnk_lst.header.next
    while pointer is not lnk_lst.trailer:
        if isinstance(pointer.data, int):
            lst_copy.add_last(pointer.data)
        else:
            lst_copy.add_last(deep_copy_linked_list(pointer.data))
        pointer = pointer.next
    return lst_copy
