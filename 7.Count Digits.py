def count_digits(text: str) -> int:
    A = list(text)
    a = 0
    for i in range(len(A)):
        if A[i].isdigit():
            a += 1
    return a
