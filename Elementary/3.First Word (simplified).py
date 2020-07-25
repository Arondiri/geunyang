def first_word(text: str) -> str:
    a = text.find(" ")
    if a == -1:
        return text
    else:
        return text[:a]
