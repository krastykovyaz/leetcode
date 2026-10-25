# Valid Palindrome
# Given a string s, return true if it is a palindrome, otherwise return false.

# A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

# Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

# Example 1:

# Input: 
s = "Was it a car or a cat I saw?"

# Output: true
# Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

def is_palindrom(s):
    start = 0
    end = len(s) - 1
    mid = len(s) // 2
    while end > mid and start < mid:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True

if __name__=='__main__':
    s = "wasitacaroracatisaw"
    print(is_palindrom(s))

