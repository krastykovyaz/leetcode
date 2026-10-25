a = [1, 2, 3, 2, 0]
b = [5, 1, 2, 7, 3, 2]
# out [1, 2, 2, 3]

counter_b = {}
for i in range(len(b)):
    if b[i] not in counter_b:
        counter_b[b[i]] = 1
    else:
        counter_b[b[i]] += 1

result = []
for i in range(len(a)):
    if a[i] in counter_b and counter_b[a[i]] > 0:
        counter_b[a[i]] -= 1
        result.append(a[i])

print(result)
