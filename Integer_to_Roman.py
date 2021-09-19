class Solution:
    def intToRoman(self, num: int) -> str:
        m = ["", "M", "MM", "MMM"]
        c = ["", "C", "CC", "CCC", "CD", "D",
             "DC", "DCC", "DCCC", "CM"]
        x = ["", "X", "XX", "XXX", "XL", "L",
             "LX", "LXX", "LXXX", "XC"]
        i = ["", "I", "II", "III", "IV", "V",
             "VI", "VII", "VIII", "IX"]
        res_m = m[num // 1000]
        res_c = c[num % 1000 // 100]
        res_x = x[(num % 100) // 10]
        res_i = i[num % 10]
        ans = res_m + res_c + res_x + res_i
        return ans





if __name__=='__main__':
    s = Solution()
    print(s.intToRoman(1994))
