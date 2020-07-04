def first_word(text: str) -> str:
    a = 0
    b = 0
    for i in range(len(text)):
        if text[i] != " " and text[i] != "," and text[i] != ".":
            a = i
            break
    if ' ' in text[a:] or ',' in text[a:] or '.' in text[a:]:
        for i in range(a,len(text)):
            if text[i] == " " or text[i] == "," or text [i] == ".":
                b = i
                break
        return text[a:b]
    else:
        return text[a:]
