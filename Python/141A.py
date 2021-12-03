guest = input() + input()
heap = input()

if len(guest) != len(heap):
    print('NO')
    exit()
else:
    for i in guest:
        if guest.count(i) != heap.count(i):
            print('NO')
            exit()

print('YES')