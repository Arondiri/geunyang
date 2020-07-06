def between_markers(text: str, begin: str, end: str) -> str:
    if begin not in text and end not in text:
        return text
    elif begin not in text and end in text:
        return text[:text.index(end)]
    elif begin in text and end not in text:
        return text[text.index(begin)+len(begin):]
    else:
        if text.index(begin) < text.index(end):
            return text[text.index(begin)+len(begin):text.index(end)]
        elif text.index(begin) > text.index(end):
            return ''
