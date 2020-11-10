summ = input()

c1 = c2 = c3 = 0

for i in range(0, len(summ), 2):
    if summ[i] == '1':
        c1 += 1
    elif summ[i] == '2':
        c2 += 1
    else:
        c3 += 1

ss = "1+" * c1 + "2+" * c2 + "3+" * c3
print(ss[:-1])