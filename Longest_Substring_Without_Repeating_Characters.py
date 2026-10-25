# Given a string s, find the length of the longest substring without duplicate characters.

 

# Example 1:

# Input: 
s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

def find_lenght(s):
    storage = {}
    max_len = 0
    l = 0
    for r, val in enumerate(s):
        if val in storage and storage[val] >= l:
            l = storage[val] + 1
        storage[val] = r
        max_len = max(max_len, r - l + 1)
    return max_len


if __name__=='__main__':
    s = "pwwkew"
    print(find_lenght(s))    


