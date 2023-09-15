from ChainingHashTableMap import ChainingHashTableMap
from DoublyLinkedList import DoublyLinkedList

def fist_unique(lst):
    hmap = ChainingHashTableMap()
    for i in lst:
        if i not in hmap:
            hmap[i] = 0
        hmap[i] += 1

    for i in lst:
        if hmap[i] == 1:
            return i


lst = [5, 9, 2, 9, 0, 5, 9, 7]
print(fist_unique(lst))


def two_sum(lst, target):
    hmap = ChainingHashTableMap()
    for i in range(len(lst)):
        hmap[target - lst[i]] = (i, target - lst[i])

    for c in range(len(lst)):
        if lst[c] in hmap:
            if hmap[lst[c]][0] == c:
                pass
            else:
                return hmap[lst[c]][0], c
        return (None, None)


lst2 = [-2, 11, 15, 21, 20, 20]
print(two_sum(lst2, 22))


class PlayList:
    def __init__(self):
        self.hmap = ChainingHashTableMap()
        self.dll = DoublyLinkedList()

    def add_song(self, new_song_name):
        self.hmap[new_song_name] = self.dll.add_last(new_song_name)

    def add_song_after(self, song_name, new_song_name):
        self.hmap[new_song_name] = self.dll.add_after(self.hmap[song_name], song_name)

    def play_song(self, song_name):
        print("Playing "+self.hmap[song_name].data)

    def play_list(self):
        for song in dll:
            print("Playing "+ song)
