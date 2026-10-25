inp = [(1, 5), (100, 200), (2, 4)]
out = [(1, 4), (100, 200)]


sort_inp = sorted(inp)
merged = [list(sort_inp[0])]
for start, end in sort_inp[1:]:
    print(merged)
    last_edge = merged[-1][1]
    if start < last_edge:
        merged[-1][1] = max(end, last_edge)
    else:
        merged.append([start, end])

    
print(merged)
    


