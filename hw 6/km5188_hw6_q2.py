from DoublyLinkedList import DoublyLinkedList


class Integer:
    def __init__(self, num_str):
        self.data = DoublyLinkedList()
        self.num_lst = list(str(num_str))

        for i in self.num_lst:
            self.data.add_last(int(i))

    def __add__(self, other):
        p1 = self.data.trailer.prev
        p2 = other.data.trailer.prev

        r = DoublyLinkedList()
        rem = 0

        while p1.prev is not None and p2.prev is not None:
            res = int(p1.data) + int(p2.data) + rem
            rem = 0
            if res >= 10:
                reslst = list(str(res))
                rem = int(reslst[-2])
                r.add_first(int(reslst[-1]))
            else:
                r.add_first(res)

            p1 = p1.prev
            p2 = p2.prev

        while p1.prev is not None:
            res = rem + int(p1.data)
            rem = 0
            if res >= 10:
                reslst = list(str(res))
                rem = int(reslst[-2])
                r.add_first(int(reslst[-1]))
            else:
                r.add_first(res)

            p1 = p1.prev

        while p2.prev is not None:
            res = rem + int(p2.data)
            rem = 0
            if res >= 10:
                reslst = list(str(res))
                rem = int(reslst[-2])
                r.add_first(int(reslst[-1]))
            else:
                r.add_first(res)

            p2 = p2.prev

        if rem != 0:
            r.add_first(rem)

        output_s = ''.join(str(i) for i in r)
        return Integer(output_s)

    def __repr__(self):
        while self.data.header.next.data == 0:
            self.data.delete_first()
        return "".join([str(elem) for elem in self.data])

    def __mul__(self, other):
        p1 = self.data.trailer.prev
        res = 0
        for i in range(len(self.data)):
            p2 = other.data.trailer.prev
            rem = 0
            zeros = "0" * i
            for j in range(len(other.data)):
                mul = int(p1.data) * int(p2.data) + rem
                if mul >= 10:
                    reslst = list(str(mul))
                    rem = int(reslst[-2])
                    zeros = str(reslst[-1]) + zeros
                else:
                    rem = 0
                    zeros = str(mul) + zeros
                p2 = p2.prev
            p1 = p1.prev
            if rem != 0:
                zeros = str(rem) + zeros
            res += int(zeros)
        return res


