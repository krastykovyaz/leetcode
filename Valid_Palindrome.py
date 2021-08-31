class Solution:
    def IsPalindrom(self, s: str)->bool:
        s = s.lower()
        new_s = ''
        for chr in s:
            if chr in "abcdefjhigklmnopqrstuvw":
                new_s += chr
        s = new_s
        length = len(s)
        i = 0
        if length % 2:
            if s[::-1][:length // 2 - 1] != s[:length // 2 - 1]:
                return False
        else:
            if s[::-1][:length // 2] != s[:length // 2]:
                return False
        return True


if __name__=='__main__':
    s = Solution()
    text = "A man, a plan, a canal: Panama"
    print(s.IsPalindrom(text))