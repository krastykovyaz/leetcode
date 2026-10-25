# You are given two strings s1 and s2.
# Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a substring of s2, then return true.
# Both strings only contain lowercase letters.

# Example 1:
# Input: 
s1 = "a"
s2 = "ab"

# Output: true
# Explanation: The substring "cab" is a permutation of "abc" and is present in "lecabee".

# Example 2:
# Input: 
# s1 = "abc"
# s2 = "lecaabee"

# Output: false

def find_substring(s1 ,s2):
    if len(s1) > len(s2):
        return False
    need = [0] * 26
    window = [0] * 26
    for c1 in s1:
        need[ord(c1) - ord('a')] += 1
    k = len(s1)
    for c2 in s2[:k]:
        window[ord(c2) - ord('a')] += 1
    left = 0
    for right in range(k, len(s2)):
        
        print(s2[left], s2[right], window)
        if need == window:
            return True
        window[ord(s2[right]) - ord('a')] += 1
        window[ord(s2[left]) - ord('a')] -= 1
        left += 1
    return False

if __name__=='__main__':
    print(find_substring(s1,s2))
