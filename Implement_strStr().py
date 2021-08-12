class Solution:
    def FirstIndex(self, haystack: str, needle: str)->int:
        i = 0
        if needle in haystack:
            while i < (len(haystack)):
                j = 0
                while j < len(needle) and haystack[i] == needle[j]:
                    j += 1
                    i += 1
                if j + 1 == len(needle):
                    return i - j - 1
                i = i - j
                i += 1
        else:
            return -1
        return i

if __name__=='__main__':
    haystack = "aaaaa"
    needle = "bba"
    s = Solution()
    print(s.FirstIndex(haystack, needle))
