n = list(map(int, input().split()))
h = list(map(int, input().split()))

answer = 0

for i in h:
    if i > n[1]:
        answer += 2
    else:
        answer += 1

print(answer)
