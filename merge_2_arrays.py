from typing import List

def loop(a: List[int], b: List[int]) -> List[int]:
    sorted_list = []
    i = 0
    j = 0
    length = len(a) + len(b)
    while j < length:
        if len(b) and len(a):
            if a[i] < b[i]:
                sorted_list.append(a[i])
                a = a[1:]
            else:
                sorted_list.append(b[i])
                b = b[1:]
        else:
            if len(b) > len(a):
                sorted_list.extend(b)
            else:
                sorted_list.extend(a)
            break
        j += 1

    return sorted_list





def merge(a: List[int], b: List[int]) -> List[int]:
    if a[0] < b[0]:
        return loop(a, b)
    return loop(b, a)



if __name__ == '__main__':
    a = [1, 3, 5, 7, 9]
    b = [2, 4, 8, 10, 12, 13]
    print(merge(a,b))