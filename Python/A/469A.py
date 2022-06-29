t = int(input())

a = list(map(int, input().split()))[1:]
b = list(map(int, input().split()))[1:]
result = set(a)
result.update(b)
print("I become the guy." if len(result) == t else "Oh, my keyboard!")
