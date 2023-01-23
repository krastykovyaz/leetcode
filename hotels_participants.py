from typing import List
from collections import defaultdict


def check_partic(a: List[tuple]) -> int:
    arrive = defaultdict(int)
    depart = defaultdict(int)
    for item in a:
        arrive[item[0]] += 1
        depart[item[1]] += 1
    current = 0
    res = 0
    for day in sorted(set(arrive.keys() | depart.keys())):
        current -= depart[day]
        current += arrive[day]
        if current > res:
            res = current
    return res


if __name__ == '__main__':
    sample = [(1, 2), (1, 3), (2, 4), (2, 3), ]
    print(check_partic(sample))
