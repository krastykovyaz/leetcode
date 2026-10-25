line = 'AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB'
# out A4B3C2XYZD4E3F3A6B28

def reduce_line(line):
    if len(line) == '' or len(line) == 1:
        return line
    else:
        res = []
        line = list(line) + [None]
        cur = line[0]
        count = 0
        for i, sym in enumerate(line):
            if sym == cur:
                count += 1
            else:
                if count > 1:
                    res.append(f"{cur}{count}")
                else:
                    res.append(f"{cur}")
                count = 1
                cur = line[i]
        return res


print(reduce_line(line))
    