def popular_words(text: str, words: list) -> dict:
    A = text.split()
    B = {}
    for i in range(len(A)):
        A[i] = A[i].lower()
    for i in words:
        B[i] = A.count(i.lower())
    return B
