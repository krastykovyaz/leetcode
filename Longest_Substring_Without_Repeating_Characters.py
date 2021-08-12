import timeit

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c_list = {}
        length = 0
        anchor = 0
        for i, c in enumerate(string):
            if c in c_list and c_list[c] >= anchor:
                anchor = c_list[c] + 1
            else:
                length = max(length, length + 1 - anchor)
            c_list[c] = i
        return length




if __name__=='__main__':
    string = "abcabcbb"
    s = Solution()
    print(s.lengthOfLongestSubstring(string))
    print(timeit.timeit(lambda: s.lengthOfLongestSubstring(string), number=1))
