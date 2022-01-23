from itertools import combinations

print(sum(map(lambda x: (x == ('Q', 'A', 'Q')), combinations(input(), 3))))
