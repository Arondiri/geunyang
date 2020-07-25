def nearest_value(values: set, one: int) -> int:
    A = []
    B = list(values)
    C = []
    for i in range(len(B)):
        A.append(abs(B[i]-one))
    for i in range(len(B)):
        if A[i] == min(A):
            C.append(B[i])
    return min(C)
