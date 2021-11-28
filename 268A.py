a = int(input())

forms = []
for i in range(a):
    forms.append([int(x) for x in input().split()])

away_form = 0
for i in range(a):
    for game in range(i+1, a):
        if forms[i][0] == forms[game][1]:
            away_form += 1
        if forms[i][1] == forms[game][0]:
            away_form += 1

print(away_form)
