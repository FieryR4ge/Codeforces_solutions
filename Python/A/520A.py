a = int(input())
b = str(input())


def check_word(word: str) -> None:
    word = set(word.lower())
    if len(word) < 26:
        print("NO")
    else:
        print("YES")


check_word(b)
