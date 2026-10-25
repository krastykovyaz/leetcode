# You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.

# After performing at most k replacements, return the length of the longest substring which contains only one distinct character.

# Example 1:
# Input: 
s = "XYYX"
k = 2

# Output: 4
# Explanation: Either replace the 'X's with 'Y's, or replace the 'Y's with 'X's.

# Example 2:
# Input: 
# s = "AAABABB"
# k = 1

# Output: 5

def replace_chars(s, k):
    from collections import defaultdict
    storage = defaultdict(int)
    replacements = 0
    left = 0
    max_len = 0
    for right, value in enumerate(s):
        storage[value] += 1
        replacements = max(replacements, storage[value])
        while right - left + 1 - replacements > k:
            storage[s[left]] -= 1
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len

if __name__=='__main__':
    # s = "AABABBA"
    # k = 2
    print(replace_chars(s, k))