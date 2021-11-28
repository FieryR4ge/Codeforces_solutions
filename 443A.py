letter = set()

for element in list(map(str, input())):
    if element.isalpha():
        letter.add(element)

print(len(letter))
