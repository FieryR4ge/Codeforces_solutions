t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    if a == b:
        print(0)
    elif (a < b and (b-a) % 2 != 0) or (a > b and (a-b) % 2 == 0):
        print(1)
    else:
        print(2)
