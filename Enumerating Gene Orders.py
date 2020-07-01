n = 6
from itertools import permutations
per = permutations([1, 2, 3, 4, 5, 6])
list_per = list(per)
print(len(list_per))
for i in list_per:
    print(' '.join(map(str, i)))
