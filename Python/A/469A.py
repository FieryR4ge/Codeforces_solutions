a = int(input()) 

lvl = set()

for i in range(2):
    l = list(map(int, input().split())) 
    l = l[1:]
    lvl.update(l)


for i in range(a): 
    if not (i + 1) in lvl:
        print("Oh, my keyboard!")
        quit()

print("I become the guy.")