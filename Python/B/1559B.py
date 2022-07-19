for _ in range(int(input())):
    n = int(input())
    s = str(input())
    if s == '?' * n:
        s = s.replace('?', 'R', 1)

    while '?' in s:
        s = s.replace('R?', 'RB')
        s = s.replace('B?', 'BR')
        s = s.replace('?R', 'BR')
        s = s.replace('?B', 'RB')

    print(s)
