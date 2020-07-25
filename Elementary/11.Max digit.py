def max_digit(number: int) -> int:
    A = []
    if number == 0:
        return 0
    else:
        while number//10 != 0:
            A.append(number%10)
            number = number//10
        A.append(number%10)
        return max(A)
