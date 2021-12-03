a, b = map(int, input().split())

count_task = 0
count = 0

for i in range(a):
    count_task += (i+1) * 5
    if count_task <= 240 - b:
        count += 1

print(count)
