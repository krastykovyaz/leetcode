ar = [0, 0, 1, 1, 0, 1, 1, 0]

def looking_seq(ar):
    len_arr = len(ar)
    n = sum(ar)
    if len_arr == n:
        return n - 1
    cur = 0
    prev = 0
    max_len = 0
    for num in ar:
        if num == 1:
            cur += 1
        else:
            max_len = max(max_len, prev + cur)
            prev = cur
            cur = 0
    max_len = max(max_len, prev + cur)
    return max_len

print(looking_seq(ar))