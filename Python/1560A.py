n = int(input())

array = [i for i in range(0, 1670) if i % 3 != 0 and not str(i).endswith('3')]

for _ in range(n):
    k = int(input())
    print(array[k-1])
