from math import floor, sqrt
from sys import set_int_max_str_digits

def is_prime(n: int) -> bool:
    """Check whether $n$ is prime or not."""
    if n <= 1: return False
    for k in range(2, floor(sqrt(n))+1):
        if n % k == 0:
            return False
    return True

__current_pn = 1
def next_prime() -> int:
    global __current_pn
    __current_pn += 1
    while not is_prime(__current_pn): __current_pn += 1
    return __current_pn

def opcode_to_int(c: str) -> int:
    match c:
        case '>': return 1
        case '<': return 2
        case '+': return 3
        case '-': return 4
        case '[': return 5
        case ']': return 6
        case ',': return 7
        case '.': return 8
        case _:   return 0

set_int_max_str_digits(1_000_000_000)

n = 1
program = input()

for opcode in program: n = n * next_prime()**(opcode_to_int(opcode)) if opcode_to_int(opcode) != 0 else n

print(n)