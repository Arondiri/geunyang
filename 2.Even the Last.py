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
