t = int(input())
numbers = list(map(int, input().split()))
positive = []
negative = []

for number in numbers:
    if number >= 0:
        positive.append(abs(1 - number))
    else:
        negative.append(abs(-1 - number))

ans = sum(positive) + sum(negative)

if len(negative) & 1:
    if 0 not in numbers:
        ans += 2

print(ans)
