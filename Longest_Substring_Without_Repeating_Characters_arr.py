# Given a string s, find the length of the longest substring without duplicate characters.

# A substring is a contiguous sequence of characters within a string.

# Example 1:

# Input: 
s = "zxyzxyz"

# Output: 3
# Explanation: The string "xyz" is the longest without duplicate characters.

# Example 2:

# Input: 
# s = "bbbbb"

# Output: 1

def find_long(s):
    used = set()
    max_len = 0
    l = 0
    for r,c in enumerate(s):
        while c in used:
            used.remove(s[l])
            l += 1
        used.add(c)
        max_len = max(max_len, r - l + 1)
    return max_len

if __name__=='__main__':
    print(find_long(s))