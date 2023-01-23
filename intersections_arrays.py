from typing import List

def looking_4_repeats(a:List[int], b:List[int]) -> List[int]:
    result = []
    for i in range(len(a)):
        if a[i] in b:
            result.append(a[i])
    return result



if __name__ == '__main__':
    a = [1,2,3,2,0]
    b = [5,1,2,7,3,2]
    print(looking_4_repeats(a, b))