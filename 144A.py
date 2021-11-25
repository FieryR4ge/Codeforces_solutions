qty = int(input())
height = list(map(int, input().split()))

result = height.index(max(height)) + height[::-1].index(min(height))

print(result - (result >= qty))
