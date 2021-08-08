a = int(input())
friends = list(map(int, input().split()))

answer = {}

for k, v in enumerate(friends):
    answer[v] = k + 1

for i in range(len(friends)):
    print(answer[i+1])
