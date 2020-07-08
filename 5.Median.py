from typing import List

def checkio(data: List[int]) -> [int, float]:
    data.sort()
    if len(data)%2 != 0:
        return data[len(data)//2]
    else:
        return (data[(len(data)-1)//2]+data[(len(data)+1)//2])/2
