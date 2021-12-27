a, b = map(int, input().split())

n = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 0]

index_a = n.index(a)

if index_a == len(n) - 1:
    print("NO")
else:
    if n[index_a + 1] == b:
        print("YES")
    else:
        print("NO")
