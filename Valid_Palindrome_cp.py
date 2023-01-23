from typing import List

class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789'
        s = s.lower()
        flag = False
        for i in range(len(s)):
            if s[i] in alphabet:
                s = s[i:]
                flag = True
                break
        for i in range(len(s))[::-1]:
            if s[i] in alphabet:
                s = s[:i+1]
                flag = True
                break
        if flag == False:
            return True
        length = len(s)
        i = 0
        j = length - i - 1
        left = []
        right = []
        while i < length // 2 and j >= length // 2:
            step = 0
            while s[i + step] not in alphabet:
                step += 1
            i += step
            step = 0
            while s[j - step] not in alphabet:
                step += 1
            j -= step
            left.append(s[i])
            right.append(s[j])
            i += 1
            j -= 1
        print(left, right)
        if left != right:
            return False
        return True


if __name__=='__main__':
    string = "Salisbury moor, sir, is roomy. Rub Silas."
    s = Solution()
    print(s.isPalindrome(string))

