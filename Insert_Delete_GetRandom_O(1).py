import random


class RandomSet:
    def __init__(self):
        self.MyList = []
        self.MyDict = {}

    def insert(self, val: int) -> bool:
        if val in self.MyDict:
            return False
        idx = len(self.MyList) - 1
        self.MyList.append(val)
        self.MyDict[val] = idx
        return True

    def remove(self, val: int) -> bool:
        if val not in self.MyDict:
            return False
        tmp_idx = self.MyDict[val]
        last = len(self.MyList) - 1
        temp = self.MyList[last]
        self.MyDict[temp] = tmp_idx
        self.MyList[tmp_idx] = temp
        self.MyList.pop()
        del self.MyDict[val]
        return True


    def getRandom(self) -> int:
        return random.choice(self.MyList)


if __name__ == '__main__':
    val = 5
    obj = RandomSet()
    param_1 = obj.insert(3)
    param_1 = obj.insert(4)
    param_1 = obj.insert(6)
    param_2 = obj.remove(6)
    param_3 = obj.getRandom()
    print(param_1, param_2, param_3)
