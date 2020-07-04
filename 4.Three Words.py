def checkio(words: str) -> bool:
    A = list(words)
    a = 0
    for i in words.split():
        if i.isalpha():
            a += 1
        else:
            a = 0
        if a == 3:
            return True
    return False
