from time import time
from typing import Optional, Tuple

def lcg() -> int:
    a: int = 1103515245
    c: int = 12345
    m: int = 2**31
    seed: float = time()*1_000
    return int((a*seed+c) % m)

def getRandomNumber(range: Optional[Tuple[int,int]] = None) -> int:
    a: int = 1103515245
    c: int = 12345
    m: int = 2**31
    xn: int = (a*lcg()+c) % m
    if range is None:
        range = [0,m-1]
    return int((xn/(m-1)) * (range[1] - range[0]) + range[0])

