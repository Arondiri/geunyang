def beginning_zeros(number: str) -> int:
    A = list(number)
    a = 0
    for i in range(len(A)):
        if A[i] == "0":
            a += 1
        else:
            break
    return a
