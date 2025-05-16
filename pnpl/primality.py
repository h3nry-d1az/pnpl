"""This module contains prime-related functions, which serve as the core algorithms behind PNPL because of its foundations in the fundamental theorem of arithmetic."""
from typing import Tuple, Set
from math import floor, sqrt

def factor(n: int, __start: int = 2) -> Set[Tuple[int, int]]:
    r"""Decompose $n$ into its prime factors, represented as a set with tuples of the form $(p_k, \alpha_k)$, where $p_k$ is each prime dividing $n$ and $\alpha_k$ its exponent."""
    factors = set()
    m = n
    for pk in range(__start, n):
        if n % pk == 0:
            alphak = 0
            while m % pk == 0:
                alphak += 1
                m //= pk
            factors.add((pk, alphak))
            factors |= factor(m, pk+1)
            break
    if m == n and m != 1: factors.add((m, 1))
    return factors

def is_prime(n: int) -> bool:
    """Check whether $n$ is prime or not."""
    if n <= 1: return False
    for k in range(2, floor(sqrt(n))+1):
        if n % k == 0:
            return False
    return True

__current_pn = 1
def next_prime() -> int:
    """An impure function that returns the next prime number after each call."""
    global __current_pn
    __current_pn += 1
    while not is_prime(__current_pn): __current_pn += 1
    return __current_pn

def reset_prime_counter() -> None:
    """Resets the state of the `next_prime` function."""
    global __current_pn
    __current_pn = 1