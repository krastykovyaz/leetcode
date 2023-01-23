from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1
        result = []
        i = 0
        count = 1
        while i < len(chars):
            if chars[i] not in result:
                if count > 1:
                    result.append(str(count))
                result.append(chars[i])
                count = 1
            else:
                count += 1
            if i + 1 == len(chars) and count > 1:
                result.append(str(count))
            i += 1
        return len(''.join(result))


if __name__ == '__main__':
    s = Solution()
    chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    print(s.compress(chars))
