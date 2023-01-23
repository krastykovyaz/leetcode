from typing import List


def get_delta(a: List[int]) -> str:
    b = sorted(a)
    print(b)
    start = f'{b[0]}'
    i = 1
    flag = False
    block = False
    while i < len(b):
        if b[i - 1] + 1 == b[i]:
            flag = True
            block = True

        else:
            if block == True:
                start += '-'
                start += f'{b[i - 1]}'
            start += ','
            start += f'{b[i]}'
            flag = False
        i += 1
    if flag == True and block == True:
        start += '-'
        start += f'{b[i - 1]}'
    return start


if __name__ == '__main__':
    initial_list = [1, 4, 5, 2, 3, 9, 8, 11, 0, 12, 19]
    print(get_delta(initial_list))
