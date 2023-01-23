from typing import List

def checker(s: str, counter: int, i: int, new_string:str)->str:
    if s[i - 1] == s[i]:
        counter += 1
    else:
        new_string += s[i - 1]
        new_string += str(counter)
        counter = 1
    return counter, new_string

def count_cahrs(s: str) -> str:
    i = 1
    counter = 1
    new_string = ''
    while i < len(s):
        counter, new_string = checker(s, counter, i, new_string)
        i += 1
    if new_string != '' and s[i - 1] == new_string[-1]:
        counter += 1
        new_string += s[i] + str(counter)
    else:
        new_string += s[i - 1]
        new_string += str(counter)
    return new_string



if __name__=='__main__':
    string = 'AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBBAA'
    print(count_cahrs(string))