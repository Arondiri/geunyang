def backward_string_by_word(text: str) -> str:
    A = text.split()
    B = []
    t = text
    C = []
    D = []
    d = 0
    E = []
    e = 0
    if A == []:
        return ''
    else:
        for i in range(len(A)):
            B.append([])
            for j in range(len(A[i])):
                B[i].append(A[i][-j-1])
            B[i] = ''.join(B[i])
            d += len(A[i])
            D.append(d)
        for i in A:
            C.append(t.index(i))
            t = t[t.index(i)+len(i):]
        a = list(text).count(' ')
        for i in range(len(C)):
            e += C[i]
            E.append(e)
        if a == 0:
            return B[0]
        else:
            for i in range(len(B)-1):
                B[i] = B[i]+text[E[i]+D[i]:E[i+1]+D[i]]
            return ''.join(B)

#%%
def backward_string_by_word(text):
    return ' '.join(word[::-1] for word in text.split(' '))
#라고 하니까 너무 간단하고;;
