a, b = map(int, input().split())
l = list(map(int, input().split()))
l = sorted(l)

l = l[::-1]
c = l[b-1]
d = 0

for i in l:
    if i >= c and i > 0:
        d += 1


print(d)