# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:
# Input: 
s = "racecar"
t = "carrace"
# Output: true
# Example 2:
# Input: 
# s = "jar"
# t = "jam"
# Output: false
# Constraints:
# s and t consist of lowercase English letters.

def is_anagrams(s, t):
    if len(s) != len(t):
        return False
    storage = [0] * 26
    for c in s:
        storage[ord(c) - ord('a')] += 1
    for c in t:
        storage[ord(c) - ord('a')] -= 1
    return True if storage == [0] * 26 else False
    


if __name__=='__main__':
    print(is_anagrams(s, t))