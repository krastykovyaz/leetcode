class Solution:
    def isValid(self, s: str) -> bool:
        while len(s):
            l = len(s)
            s = s.replace('{}', '').replace('[]', '').replace('()', '')
            if len(s) == l:
                return False
        return True



if __name__ == '__main__':
    s = Solution()
    string = '[{}][({})]'
    print(s.isValid(string))
