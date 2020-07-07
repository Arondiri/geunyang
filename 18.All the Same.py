from typing import List, Any

def all_the_same(elements: List[Any]) -> bool:
    b = len(elements)
    if b == 0:
        return True
    else:
        a = elements[0]
        for i in range(len(elements)):
            if elements[i] == a:
                b -= 1
        if b == 0:
            return True
        else:
            return False
