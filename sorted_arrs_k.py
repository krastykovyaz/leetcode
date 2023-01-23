from typing import List

def bin_search(a: List[int], k: int) -> int:
    mid = len(a) // 2
    if len(a) == 1 and k == a[0]:
        return k
    if len(a) == 1:
        return False
    if a[mid] == k:
        return a[mid]
    if a[mid] > k:
        return bin_search(a[:mid], k)
    elif a[mid] < k:
        return bin_search(a[mid:], k)


def get_sum(a: List[int], b: List[int], k: int) -> List[tuple]:
    result = []
    for i in range(len(a)):
        k_ = k - a[i]
        val = bin_search(b, k_)
        if val:
            result.append((a[i], val))
    return result


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 9]
    b = [3, 5, 6, 10, 33]
    k = 10
    print(get_sum(a, b, k))
