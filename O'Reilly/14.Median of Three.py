from typing import Iterable

def median_three(els: Iterable[int]) -> Iterable[int]:
    A = []
    for i in range(len(els)):
        if i < 2:
            A.append(els[i])
        else:
            B = [els[i-2],els[i-1],els[i]]
            B.sort()
            A.append(B[1])
    return A
