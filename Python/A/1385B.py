from typing import List


def solve(array: List) -> List:
    seen = set()
    seen_add = seen.add
    return [x for x in array if not (x in seen or seen_add(x))]


t = int(input())

for _ in range(t):
    n = int(input())
    k = list(map(int, input().split()))
    print(*solve(k))


