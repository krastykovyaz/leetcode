# Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

# Please implement encode and decode

# Example 1:

# Input: 
# strs = ["neet","code","love","you"]

# Output:["neet","code","love","you"]
# Example 2:

# Input: 
# strs = ["we","say",":","yes"]

# Output: ["we","say",":","yes"]

from typing import List

SYMBOL = '#'

def encode(strs: List[str]) -> str:
    out = []
    for st in strs:
        st_len = str(len(st))
        out.append(f"{st_len}{SYMBOL}{st}")
    return ''.join(out)

   

def decode(strs: List[str]) -> str:
    decoded = []
    i = 0
    while i < len(strs):
        j = i
        while strs[j] != SYMBOL:
            j += 1
        count = int(strs[i:j])
        j += 1
        decoded.append(strs[j:j+count])
        i = j+count
    return decoded

    

if __name__=='__main__':

    print(decode(encode(strs)))