n = int(input())

for i in range(n):
    number = int(input())
    answer = []

    temp_str = str(number)
    length = len(temp_str)

    for j in range(length):
        if temp_str[-j-1] != '0':
            answer.append(int(temp_str[-j-1]) * (10 ** j))
    print(len(answer))
    print(" ".join(map(str, answer)))
