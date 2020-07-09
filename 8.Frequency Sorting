def frequency_sorting(numbers):
    A = []
    B = []
    for i in range(len(numbers)):
        if numbers[i] not in A:
            A.append(numbers[i])
            B.append(numbers.count(numbers[i]))
    B.sort(reverse=True)
    C = [[] for i in range(len(B))]
    for i in A:
        for j in range(len(B)):
            if numbers.count(i) == B[j]:
                C[j].append(i)
                break
    for i in range(len(C)):
        C[i].sort()
    B = [[numbers.count(C[i][j]) for j in range(len(C[i]))] for i in range(len(C))]
    D = []
    for i in range(len(C)):
        for j in range(len(C[i])):
            while B[i][j] != 0:
                D.append(C[i][j])
                B[i][j] -= 1
    return D
