n = int(input())

teams = [[], [], []]

for index, value in enumerate(input().split()):
    teams[int(value) - 1].append(index + 1)

print(min(map(len, teams)))

for i in zip(*teams):
    print(i[0], i[1], i[2])
