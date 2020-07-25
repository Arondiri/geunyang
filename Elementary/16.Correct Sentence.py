def correct_sentence(text: str) -> str:
    A = list(text)
    if A[len(A)-1] != ".":
        A.append(".")
    A[0] = A[0].upper()
    return "".join(A)
