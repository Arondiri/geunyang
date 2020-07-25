def between_markers(text: str, begin: str, end: str) -> str:
    A = list(text)
    B = []
    for i in range(len(A)):
        if A[i] == begin:
            B.append(i)
        elif A[i] == end:
            B.append(i)
    C = A[B[0]+1:B[1]]
    return "".join(C)
