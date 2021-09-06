from typing import List


class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.v1 = v1
        self.v2 = v2
        self.len1 = len(v1)
        self.len2 = len(v2)
        self.idx1 = 0
        self.idx2 = 0
        self.turn = True if self.len1 > 0 else False

    def next(self) -> int:
        if self.turn == True:
            ret = self.v1[self.idx1]
            self.idx1 += 1
            if self.idx1 < self.len2: self.turn = False
            return ret
        else:
            ret = self.v2[self.idx2]
            self.idx2 += 1
            if self.idx2 < self.len1: self.turn = True
            return ret

    def hasNext(self) -> bool:
        return self.idx1 < self.len1 or self.idx2 < self.len2


if __name__ == '__main__':
    s = ZigzagIterator([1, 4, 7], [2, 5, 8, 9])
    while s.hasNext():
        print(s.next())
