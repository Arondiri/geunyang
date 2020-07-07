def second_index(text: str, symbol: str) -> [int, None]:
    if symbol in text and text.count(symbol) >= 2:
        a = text.index(symbol)
        text = text[a+len(symbol):]
        b = text.index(symbol)
        return a+b+len(symbol)
