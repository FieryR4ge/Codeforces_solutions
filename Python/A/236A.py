name = str(input())
name = dict.fromkeys(name)

if len(name) % 2 != 0:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")
