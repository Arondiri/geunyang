A = [[],[]]
    B = {}
    C = []
    if items == []:
        return []
    else:
        for i in range(len(items)):
            if A[0].count(items[i]) == 0:
                A[0].append(items[i])
                A[1].append(items.count(items[i]))
        for i in range(len(A[0])):
            B[A[0][i]] = A[1][i]
        D = sorted(B.items(), key = lambda x:x[1],reverse=True)
        for i in range(len(D)):
            D[i] = list(D[i])
        for i in range(len(D)):
            while D[i][1] != 0:
                C.append(D[i][0])
                D[i][1] -= 1
        return C
