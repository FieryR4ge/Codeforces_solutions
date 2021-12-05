n = int(input())

citizens = list(map(int, input().split()))

count = 0

for citizen in citizens:
    result = max(citizens) - citizen
    if result > 0:
        count += result

print(count)
