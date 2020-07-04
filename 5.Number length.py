def number_length(a: int) -> int:
    b = 0
    if a == 0:
        return 1
    else:
        while a != 0:
            a = a//10
            b += 1
        return b
