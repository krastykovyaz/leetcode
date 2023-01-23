from typing import List
from collections import defaultdict


def get_groups(a: List[str]) -> List[List[str]]:
    groups = defaultdict(list)
    for i in range(len(a)):
        word = ''.join(sorted(a[i]))
        groups[word].append(a[i])
    return [sorted(vals) for key, vals in groups.items()]



if __name__ == '__main__':
    inpt = ["eat", "tea", "tan", "ate", "nat", "bat"]
    output = [["ate", "eat", "tea"], ["nat", "tan"], ["bat"]]
    print(get_groups(inpt))
