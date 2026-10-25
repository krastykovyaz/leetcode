samples = [ (1, 2), (1, 3), (2, 4), (2, 3), ]

from collections import defaultdict
arrive = defaultdict(int)
depart = defaultdict(int)
count_max = 0
count = 0
for sample in samples:
    arrive[sample[0]] += 1
    depart[sample[1]] += 1


for val in sorted(set(arrive) & set(depart)):
    if val in arrive:
        count += arrive[val]
    if val in depart:
        count += depart[val]
    if count > count_max:
        count_max = count
    count = 0
print(count_max)
