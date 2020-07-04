from typing import Iterable

def remove_all_before(items: list, border: int) -> Iterable:
    if border in items:
        while items[0] != border:
            items = items[1:]
        return items
    else:
        return items
