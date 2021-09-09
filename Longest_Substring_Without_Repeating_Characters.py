import timeit

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c_dict = {}
        length, maxlen = 0, 0
        for i, c in enumerate(s):
            if c in c_dict and c_dict[c] >= maxlen:
                maxlen = c_dict[c] + 1
            else:
                length = max(length, i - maxlen + 1)
            c_dict[c] = i
        return length





if __name__=='__main__':
    string = "abcabcbb"
    s = Solution()
    print(s.lengthOfLongestSubstring(string))
    print(timeit.timeit(lambda: s.lengthOfLongestSubstring(string), number=1))
