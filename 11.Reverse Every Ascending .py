def reverse_ascending(items):
    A = []
    B = []
    for i in range(1,len(items)):
        if items[i] <= items[i-1]:
            A.append(i)
    if A == []:
        B = items[::-1]
        return B
    else:
        a = 0
        if len(items) not in A:
            A.append(len(items))
        for i in range(len(A)):
            B += items[a:A[i]][::-1]
            a = A[i]
        return B

#%%
def reverse_ascending(items):
    res=[]
    start=0
    for i in range(1,len(items)):
        if items[i]<=items[i-1]:
            res+=items[start:i][::-1]
            start=i
    return res+items[start:][::-1]   #훨씬 깔끔하죠?
