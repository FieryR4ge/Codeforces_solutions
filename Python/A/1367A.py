n = int(input())

for i in range(n):
    line = str(input())
    result = line[0]
    for index in range(1, len(line), 2):
        result += line[index]

    print(result)
