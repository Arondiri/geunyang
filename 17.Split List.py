def split_list(items: list) -> list:
    A = []
    B = []
    if len(items) == 0:
        return [[],[]]
    elif len(items) == 1:
        return [items, []]
    else:
        if len(items)%2 == 0:
            for i in range(len(items)//2):
                A.append(items[i])
            for i in range(len(items)//2,len(items)):
                B.append(items[i])
            return [A,B]
        else:
            for i in range(len(items)//2+1):
                A.append(items[i])
            for i in range(len(items)//2+1,len(items)):
                B.append(items[i])
            return [A,B]
