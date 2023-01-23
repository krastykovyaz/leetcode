from typing import List
from collections import defaultdict


def merge(ranges: List[List[int]]) -> List[List[int]]:
    if not ranges:
        return []

    res = []
    last_range = None
    for lst in sorted(ranges):
        if not last_range:
            last_range = lst
            continue
        if lst[0] <= last_range[1]:
            last_range = (last_range[0], max(lst[1], last_range[1]))
        else:
            res.append(last_range)
            last_range = lst
    else:
        res.append(last_range)
    return ranges



    # res = defaultdict()
    return range_lst

if __name__ == '__main__':
    inpt = [[1, 3],[100, 200],[2, 4]]
    out = [[1, 4],[100, 200]]
    print(merge(inpt))
