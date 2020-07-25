from typing import Iterable

def remove_all_after(items: list, border: int) -> Iterable:
    for i in range(len(items)):
        if items[i] == border:
            return items[:i+1]
    return items
