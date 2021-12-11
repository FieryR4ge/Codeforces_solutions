first = str(input())
second = str(input())

solution = ''

for i in range(len(first)):
    solution += str(int(first[i]) ^ int(second[i]))

print(solution)
