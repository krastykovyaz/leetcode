from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1

        result = []
        chr = ''
        i = 0
        while i < len(chars):
            j = i
            n = 1
            while j < len(chars) and chars[i] == chars[j]:
                j += 1
                n += 1
                chr = chars[i]
            result.append(chr)
            if n != 1:
                result.append(str(n))
            i = i + n - 1
        return len(result)


if __name__ == '__main__':
    s = Solution()
    chars = ["a","a","b","b","c","c","c"]
    print(s.compress(chars))
