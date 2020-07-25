from typing import Iterable

def replace_last(items: list) -> Iterable:
    A = [0 for i in range(len(items))]
    for i in range(len(items)):
        A[i] = items[i-1]
    return A
