def flat(A):
    B = []
    for i in range(len(A)):
        if isinstance(A[i],list):
            for j in range(len(A[i])):
                B.append(A[i][j])
        else:
            B.append(A[i])
    return B

def linum(A):
    a = 0
    for i in range(len(A)):
        if isinstance(A[i],list):
            a += 1
    return a

def flat_list(array):
    a = linum(array)
    while a != 0:
        array = flat(array)
        a = linum(array)
    return array
