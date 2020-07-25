def split_pairs(a):
    A = []
    if len(a)%2 == 0:
        for i in range(len(a)//2):
            A.append(a[2*i:2*i+2])
        return A
    else:
        for i in range((len(a)-1)//2):
            A.append(a[2*i:2*i+2])
        A.append(a[len(a)-1]+"_")
        return A
