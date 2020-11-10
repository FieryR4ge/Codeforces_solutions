friends = sorted(map(int, input().split()))

a = friends[1] - friends[0]
b = friends[2] - friends[1]
result = a + b

print(result)