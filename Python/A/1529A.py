t = int(input())

for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    min_value = min(array)
    answer = 0
    for a in array:
        if a != min_value:
            answer += 1

    print(answer)
