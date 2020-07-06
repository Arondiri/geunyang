def checkio(data: list) -> list:
    A = []
    if data == []:
        return []
    else:
        for i in range(len(data)):
            if data.count(data[i]) == 1:
                A.append(data[i])
        for i in A:
            data.remove(i)
        return data
