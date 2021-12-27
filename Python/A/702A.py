t = int(input())

numbers = list(map(int, input().split()))
s = 0
m = 0
j = 0

for i in numbers:
    if j < i:
        m += 1
    else:
        s = max(s, m)
        m = 1
    j = i

print(max(s, m))