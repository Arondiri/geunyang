def end_zeros(num: int) -> int:
    b = 0
    if num == 0:
        return 1
    else:
        while num%10 == 0:
            num = num//10
            b += 1
        return b
