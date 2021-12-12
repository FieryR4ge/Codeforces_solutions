a = list(map(int, input().split()))
turns = str(input())

result = 0
for turn in turns:
    result += a[int(turn)-1]

print(result)
