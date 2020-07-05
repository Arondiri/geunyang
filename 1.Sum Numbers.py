def sum_numbers(text: str) -> int:
    A = list(text)
    B = [[],[]]
    c = 0
    if len(A) == 1 or len(A) == 0:
        return 0
    else:
        if A[0].isdigit() and (A[1].isdigit() or A[1] == " "):
            B[0].append(A[0])
            B[1].append(0)
        if A[-1].isdigit() and (A[-2].isdigit() or A[-2] == " "):
            B[0].append(A[-1])
            B[1].append(len(A)-1)
        for i in range(1,len(A)-1):
            if A[i].isdigit() and (A[i+1].isdigit() or A[i+1] == " ") and (A[i-1].isdigit() or A[i-1] == " "):
                B[0].append(A[i])
                B[1].append(i)
        C = B[1][:-1]
        D = B[0]
        for i in C:
            if i in B[1] and i+1 in B[1]:
                D[B[1].index(i)+1] = D[B[1].index(i)]+D[B[1].index(i)+1]
                D.pop(B[1].index(i))
                B[1].remove(i)
        for i in B[0]:
            c += int(i)
        return c
#%%
#이렇게 하면 훨씬 간단하죠?
def sum_numbers(text: str) -> int:
    A = []
    for i in text.split():
        if i.isdigit():
            A.append(int(i))
    return sum(A)
