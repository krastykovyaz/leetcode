import timeit

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        c_list = {}
        anchor = 0
        for i, c in enumerate(s):
            if c in c_list and c_list[c] >= 0:
                anchor = 1 + c_list[c]
            else:
                length= max(length, length + 1 - anchor)
            c_list[c] = i
        return length





if __name__=='__main__':
    string = "abcabcbb"
    s = Solution()
    print(s.lengthOfLongestSubstring(string))
    print(timeit.timeit(lambda: s.lengthOfLongestSubstring(string), number=1))
