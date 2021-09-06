class Solution:
    def IsSubPermut(self, s1: str, s2: str) -> bool:
        m = len(s1)
        n = len(s2)
        if m > n:
            return False
        cnt1 = [0] * 26
        orda = ord("a")
        for i in range(m):
            cnt1[ord(s1[i]) - orda] += 1
        cnt2 = [0] * 26
        for i in range(n):
            cnt2[ord(s2[i]) - orda] += 1
        if cnt2 == cnt1: return True
        for i in range(m, n):
            cnt2[ord(s2[i - m]) - orda] -= 1
            cnt2[ord(s2[i]) - orda] += 1
            if cnt2 == cnt1:
                return True
        return False


if __name__ == '__main__':
    s = Solution()
    s1 = "ab"
    s2 = "eidboaoo"
    print(s.IsSubPermut(s1, s2))
