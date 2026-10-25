def isSubsequence(s: str, t: str) -> bool:
    t_collect = {}
    for i, t_ in enumerate(t):
        if t_ not in t_collect:
            t_collect[t_] = [i]
        else:
            t_collect[t_].append(i)
    for ch in s:
        if ch not in t_collect:
            return False
        indx_lst = t_collect[ch]
        start = 0
        end = len(t_collect[ch])
        prev = -1
        while start < end:
            mid = (start + end) // 2
            if prev <= start:
                start = mid + 1
            else:
                end = mid
        if start == t_collect[ch]:
            return False
    return True

        

s = "abc"
t = "ahbgdc"

print(isSubsequence(s, t))
print(isSubsequence("axc", "ahbgdc"))

