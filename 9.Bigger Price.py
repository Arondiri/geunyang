def bigger_price(limit: int, data: list) -> list:
    A = []
    B = []
    C = []
    for i in range(len(data)):
        A.append(data[i]['price'])
        C.append(data[i]['price'])
    C.sort(reverse=True)
    for i in range(limit):
        B.append(data[A.index(C[i])])
    return B
