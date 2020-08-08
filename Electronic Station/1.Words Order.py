def words_order(text: str, words: list) -> bool:
    Z = [i for i in words]
    for i in range(len(words)):
        a = words[i]
        del words[i]
        if a in words:
            return False
        words = [j for j in Z]
    A = text.split()
    B = []
    for i in range(len(words)):
        if words[i] not in A:
            return False
        else:
            B.append(A.index(words[i]))
    C = [i for i in B]
    B.sort()
    if C == B:
        return True
    else:
        return False
