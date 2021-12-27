t = int(input())

places = ""

for _ in range(t):
    places += str(input()) + "\n"


print("YES\n" + places.replace("OO", "++", 1) if "OO" in places else "NO")
