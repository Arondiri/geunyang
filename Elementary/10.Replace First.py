from typing import Iterable

def replace_first(items: list) -> Iterable:
    if items == "":
        return ""
    else:
        items.append(items[0])
        return items[1:]
