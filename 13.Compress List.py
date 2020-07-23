from typing import Iterable

def compress(items: list) -> Iterable:
    A = [i for i in range(len(items))]
    for i in range(1,len(items)):
        if items[i] == items[i-1]:
            A.remove(i)
    B = []
    for i in A:
        B.append(items[i])
    return B
