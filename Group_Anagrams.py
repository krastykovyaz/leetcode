# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:

# Input: 
strs = ["act","pots","tops","cat","stop","hat"]

# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
# Example 2:

# Input: strs = ["x"]

# Output: [["x"]]
# Example 3:

# Input: strs = [""]

# Output: [[""]]

def group_anagram(strs):
    from collections import defaultdict
    storage = defaultdict(list)   
    for item in strs:
        alphabet = [0] * 26
        for c in item:
            alphabet[ord(c) - ord('a')] += 1 
        alphabet = tuple(alphabet)
        storage[alphabet].append(item)
    return list(storage.values())


if __name__=='__main__':
    print(group_anagram(strs))