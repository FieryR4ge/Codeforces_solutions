a = int(input())

for i in range(a):
    n, k = map(int, input().split())
    first = sorted(list(map(int, input().split())))
    second = sorted(list(map(int, input().split())), reverse=True)

    for j in range(k):
        if first[j] < second[j]:
            first[j], second[j] = second[j], first[j]

    print(sum(first))


