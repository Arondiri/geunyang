def index_power(array: list, n: int) -> int:
    if len(array) > n:
        return array[n]**n
    else:
        return -1
