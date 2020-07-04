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
def checkio(array: list) -> int:
    A = []
    if len(array) == 0:
        return 0
    else:
        if len(array)%2 == 0:
            for i in range(len(array)//2):
                A.append(array[2*i])
        else:
            for i in range((len(array)+1)//2):
                A.append(array[2*i])
        a = sum(A)
        return a*array[len(array)-1]

#%%
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

#%%
def first_word(text: str) -> str:
    a = 0
    b = 0
    for i in range(len(text)):
        if text[i] != " " and text[i] != "," and text[i] != ".":
            a = i
            break
    if ' ' in text[a:] or ',' in text[a:] or '.' in text[a:]:
        for i in range(a,len(text)):
            if text[i] == " " or text[i] == "," or text [i] == ".":
                b = i
                break
        return text[a:b]
    else:
        return text[a:]

#%%
