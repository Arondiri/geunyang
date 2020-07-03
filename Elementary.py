def mult_two(num1,num2):
    return num1*num2

#%%
def easy_unpack(A):
    return (A[0],A[2],A[-2])

#%%
def first_word(text : str):
    a = text.find(" ")
    if a == -1:
        return text
    else:
        return text[:a]

#%%
def is_acceptable_password(password: str) -> bool:
    if len(password) > 6:
        return True
    else:
        return False

#%%
def number_length(a: int) -> int:
    b = 0
    if a == 0:
        return 1
    else:
        while a != 0:
            a = a//10
            b += 1
        return b

#%%
def end_zeros(num: int) -> int:
    b = 0
    if num == 0:
        return 1
    else:
        while num%10 == 0:
            num = num//10
            b += 1
        return b

#%%
def backward_string(val: str) -> str:
    a = list(val)
    a.reverse()
    b = "".join(a)
    return b

#%%
from typing import Iterable

def remove_all_before(items: list, border: int) -> Iterable:
    if border in items:
        while items[0] != border:
            items = items[1:]
        return items
    else:
        return items

#%%
def is_all_upper(text: str) -> bool:
    a = list(text)
    for i in range(len(a)):
        a[i] = a[i].upper()
    b = "".join(a)
    if b == text:
        return True
    elif b == "":
        return True
    else:
        return False

#%%
from typing import Iterable

def replace_first(items: list) -> Iterable:
    if items == "":
        return ""
    else:
        items.append(items[0])
        return items[1:]

#%%
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

#%%
def split_pairs(a):
    A = []
    if len(a)%2 == 0:
        for i in range(len(a)//2):
            A.append(a[2*i:2*i+2])
        return A
    else:
        for i in range((len(a)-1)//2):
            A.append(a[2*i:2*i+2])
        A.append(a[len(a)-1]+"_")
        return A

#%%
def beginning_zeros(number: str) -> int:
    A = list(number)
    a = 0
    for i in range(len(A)):
        if A[i] == "0":
            a += 1
        else:
            break
    return a

#%%
def nearest_value(values: set, one: int) -> int:
    A = []
    B = list(values)
    C = []
    for i in range(len(B)):
        A.append(abs(B[i]-one))
    for i in range(len(B)):
        if A[i] == min(A):
            C.append(B[i])
    return min(C)

#%%
def between_markers(text: str, begin: str, end: str) -> str:
    A = list(text)
    B = []
    for i in range(len(A)):
        if A[i] == begin:
            B.append(i)
        elif A[i] == end:
            B.append(i)
    C = A[B[0]+1:B[1]]
    return "".join(C)

#%%
def correct_sentence(text: str) -> str:
    A = list(text)
    if A[len(A)-1] != ".":
        A.append(".")
    A[0] = A[0].upper()
    return "".join(A)

#%%
def is_even(num: int) -> bool:
    if num%2 == 0:
        return True
    else:
        return False
