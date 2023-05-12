class Solution:
    def FirstIndex(self, haystack: str, needle: str)->int:
        i = 0
        flag = False
        if needle in haystack:
            while i < len(haystack):
                j = 0
                while j < len(needle):
                    z = 0
                    while haystack[i] == needle[j] and j < len(needle) - 1 and i < len(haystack) - 1:
                        z += 1
                        j += 1
                        i += 1
                    if j == len(needle) - 1:
                        return i - z
                    else:
                        break
                    j += 1
                i += 1
        else:
            return -1
        return i

if __name__=='__main__':
    haystack = "hello"
    needle = "ll"
    s = Solution()
    print(s.FirstIndex(haystack, needle))
