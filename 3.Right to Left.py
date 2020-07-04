def left_join(phrases: tuple) -> str:
    A = list(phrases)
    B = [list(A[i]) for i in range(len(A))]
    C = [[],[]]
    for i in range(len(B)):
        if B[i] == 'right':
            B[i] = 'left'
        elif len(B[i]) >=5:
            for j in range(len(B[i])-4):
                if B[i][j] == 'r' and B[i][j+1] == 'i' and B[i][j+2] == 'g' and B[i][j+3] == 'h' and B[i][j+4] == 't':
                    C[0].append(i)
                    C[1].append(j)
            for l in C[0]:
                for j in C[1]:
                    B[l][j] = 'l'
                    B[l][j+1] = 'e'
                    B[l][j+2] = 'f'
                    B[l][j+3] = 't'
                    B[l][j+4] = ''
    for i in range(len(A)):
        B[i] = ''.join(B[i])
    B = ','.join(B)
    return B
