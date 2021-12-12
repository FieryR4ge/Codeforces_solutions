t = int(input())

for _ in range(t):
    n = int(input())
    candy = list(map(int, input().split()))

    if sum(candy) % 2 or sum(candy) % 4 and 1 not in candy:
        print("NO")
    else:
        print("YES")