from typing import Iterable

def except_zero(items: list) -> Iterable:
    A = []
    B = []
    for i in range(len(items)):
        if items[i] == 0:
            A.append(i)
        else:
            B.append(items[i])
    B.sort()
    C = []
    c = 0
    if len(A) == 0:
        return B
    else:
        for i in range(len(A)):
            C += B[c:A[i]-i]
            C.append(0)
            c = A[i]-i
        C += B[c:]
        return C
