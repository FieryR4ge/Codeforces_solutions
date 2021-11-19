first = str(input())
second = str(input())

answer = ''
for f in range(len(first)):
    if first[f] == second[f]:
        answer += '0'

    else:
        answer += '1'

print(answer)
