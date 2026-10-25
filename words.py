inp = ["eat", "tea", "tan", "ate", "nat", "bat"]
out  =[ ["ate", "eat", "tea"], ["nat", "tan"], ["bat"] ]

from collections import defaultdict

final = []
dictinary = defaultdict(list)
for val in inp:
    dictinary[''.join(sorted(list(val)))].append(val)
for val in dictinary.values():
    final.append(val)
print(final)
