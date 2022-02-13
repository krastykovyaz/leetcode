class Solution:
    def romanToInt(self, s2: str) -> int:
        map_dict = {'I': 1, \
                    'V': 5, \
                    'X': 10, \
                    'L': 50, \
                    'C': 100, \
                    'D': 500, \
                    'M': 1000}
        result = int()
        i = 0
        while i < len(s2):
            f = False
            if i + 1 < len(s2) and s2[i] == 'I':
                if s2[i + 1] == 'V' or s2[i + 1] == 'X':
                    result += map_dict[s2[i+1]] - 1
                    i += 2
                    f = True
            elif i + 1 < len(s2) and s2[i] == 'X':
                if s2[i + 1] == 'L' or s2[i + 1] == 'C':
                    result += map_dict[s2[i+1]] - 10
                    i += 2
                    f = True
            elif i + 1 < len(s2) and s2[i] == 'C':
                if s2[i + 1] == 'D' or s2[i + 1] == 'M':
                    result += map_dict[s2[i+1]] - 100
                    i += 2
                    f = True
            if not f:
                result += map_dict[s2[i]]
                i += 1
        return result


if __name__ == '__main__':
    s2 = "MCMXCIV"
    solution = Solution()
    print(solution.romanToInt(s2))
