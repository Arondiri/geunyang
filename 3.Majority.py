def is_majority(items: list) -> bool:
    if items == []:
        return False
    else:
        t = items.count(True)
        f = items.count(False)
        if t > f:
            return True
        else:
            return False
