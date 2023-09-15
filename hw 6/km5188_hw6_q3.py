from DoublyLinkedList import DoublyLinkedList


class CompactString:
    def __init__(self, orig_str):
        self.data = DoublyLinkedList()

        if len(orig_str) != 0:
            orig_lst = list(orig_str)
            pointer = 0
            occ = 1
            while pointer + 1 < len(orig_lst):
                if orig_lst[pointer] == orig_lst[pointer + 1]:
                    occ += 1
                elif orig_lst[pointer] != orig_lst[pointer + 1]:
                    self.data.add_last((orig_lst[pointer], occ))
                    occ = 1
                pointer += 1
            self.data.add_last((orig_lst[pointer], occ))

    def __add__(self, other):
        res = DoublyLinkedList()

        if self.data.is_empty() and other.data.is_empty():
            return CompactString('')
        elif not self.data.is_empty() and other.data.is_empty():
            return self
        elif self.data.is_empty() and not other.data.is_empty():
            return other

        if self.data.trailer.prev.data[-2] == other.data.header.next.data[-2]:
            sum_occ = self.data.trailer.prev.data[-1] + other.data.header.next.data[-1]

            for i in self.data:
                res.add_last(i)
            res.delete_last()

            res.add_last((self.data.trailer.prev.data[-2], sum_occ))

            temp_other_first = other.data.delete_first()
            for i in other.data:
                res.add_last(i)

            other.data.add_first(temp_other_first)
        else:
            for i in self.data:
                res.add_last(i)
            for i in other.data:
                res.add_last(i)

        res_lst = []
        for tuple in res:
            for occ in range(tuple[-1]):
                res_lst.append(tuple[-2])

        res_str = "".join(res_lst)

        return CompactString(res_str)

    def __lt__(self, other):
        p1 = self.data.header.next
        p2 = other.data.header.next

        if p1 == self.data.trailer and p2 != other.data.trailer:
            return True
        elif p1 != self.data.trailer and p2 == other.data.trailer:
            return False
        elif p1 == self.data.trailer and p2 == other.data.trailer:
            return False

        while p1.next is not None and p2.next is not None:
            p1o = ord(p1.data[-2])
            p2o = ord(p2.data[-2])
            if p1o < p2o:
                return True
            elif p1o > p2o:
                return False
            elif p1o == p2o and p1.data[-1] > p2.data[-1]:
                p2 = p2.next
            elif p1o == p2o and p1.data[-1] < p2.data[-1]:
                p1 = p1.next
            elif p1o == p2o and p1.data[-1] == p2.data[-1]:
                p1 = p1.next
                p2 = p2.next
        print(p1.data, p2.data)
        if p1 == self.data.trailer and p2 != other.data.trailer:
            return True
        elif p1 != self.data.trailer and p2 == other.data.trailer:
            return False
        elif p1 == self.data.trailer and p2 == other.data.trailer:
            return False
        return False

    def __le__(self, other):
        return not self.__gt__(other)

    def __gt__(self, other):
        return other.__lt__(self)

    def __ge__(self, other):
        return not self.__lt__(other)

    def __repr__(self):
        res = []
        for tuple in self.data:
            for occ in range(tuple[-1]):
                res.append(tuple[-2])
        return "".join(res)

