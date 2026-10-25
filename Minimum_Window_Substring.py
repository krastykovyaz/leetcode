# Given two strings s and t, return the shortest substring of s such that every character in t, including duplicates, is present in the substring. If such a substring does not exist, return an empty string "".

# You may assume that the correct output is always unique.

# Example 1:

# Input: 
s = "OUZODYXAZV"
t = "XYZ"

# Output: "YXAZ"
# Explanation: "YXAZ" is the shortest substring that includes "X", "Y", and "Z" from string t.

# Example 2:

# Input: s = "xyz", t = "xyz"

# Output: "xyz"

def minWindow( s, t) -> str:
        if not t or not s:
            return ""
        from collections import Counter, defaultdict
        need = Counter(t)            # symbols
        window = defaultdict(int)              
        have = 0                     # how many symbols are satisfied
        needCount = len(need)        # q unique symbols

        res = [-1, -1]               # border of the best window
        resLen = float("inf")

        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c]  += 1

            # if friquent match +1 to have
            if c in need and window[c] == need[c]:
                have += 1

            # window is valid → try to reduce
            while have == needCount:
                # update result if window is smaller
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                # try to move left pointer
                window[s[l]] -= 1
                if s[l] in need and window[s[l]] < need[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l:r + 1] if resLen != float("inf") else ""


if __name__=='__main__':
    print(minWindow(s, t))