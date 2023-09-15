from DoublyLinkedList import DoublyLinkedList


def merge_linked_lists(srt_lnk_lst1, srt_lnk_lst2):

    def merge_sublists(l1, l2, p1, p2, res):
        if p1 == l1.trailer and p2 == l2.trailer:
            return

        elif p1 == l1.trailer:
            res.add_last(p2.data)
            p2 = p2.next

        elif p2 == l2.trailer:
            res.add_last(p1.data)
            p1 = p1.next

        elif p1.data == p2.data:
            res.add_last(p1.data)
            res.add_last(p2.data)
            p1 = p1.next
            p2 = p2.next

        elif p1.data > p2.data:
            res.add_last(p2.data)
            p2 = p2.next

        elif p1.data < p2.data:
            res.add_last(p1.data)
            p1 = p1.next
        merge_sublists(l1, l2, p1, p2, res)
        return res
    return merge_sublists(srt_lnk_lst1, srt_lnk_lst2, srt_lnk_lst1.header.next, srt_lnk_lst2.header.next, DoublyLinkedList())



