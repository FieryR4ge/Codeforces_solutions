number = str(input())

happy_counter = 0

for i in number:
    if i == '4' or i == '7':
        happy_counter += 1

if happy_counter == 4 or happy_counter == 7:
    print('YES')
else:
    print('NO')
