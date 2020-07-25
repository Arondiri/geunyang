def is_all_upper(text: str) -> bool:
    a = list(text)
    for i in range(len(a)):
        a[i] = a[i].upper()
    b = "".join(a)
    if b == text:
        return True
    elif b == "":
        return True
    else:
        return False
