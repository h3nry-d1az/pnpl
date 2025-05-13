from typing import List, Tuple, Set
from enum import Enum

from sys import set_int_max_str_digits

set_int_max_str_digits(1_000_000_000)

def factor(n: int) -> Set[Tuple[int, int]]:
    r"""Factors $n$ into its prime factors, represented as a set with tuples of the form $(p_k, \alpha_k)$."""
    factors = set()
    m = n
    for pk in range(2, n):
        if n % pk == 0:
            alphak = 0
            while m % pk == 0:
                alphak += 1
                m //= pk
            factors.add((pk, alphak))
            factors |= factor(m)
            break
    if m == n and m != 1: factors.add((m, 1))
    return factors

class Opcode(Enum):
    INC_PTR = 1
    DEC_PTR = 2
    ADD     = 3
    SUB     = 4
    LOOP_ST = 5
    LOOP_EN = 6
    GETCH   = 7
    PUTCH   = 8

class PNPL:
    memory: List[int]
    pointer: int = 0
    program: List[Opcode]
    program_counter: int = 0
    loop_stack: List[int]
    __level: int = 0

    def __init__(self, program: int, memory_size: int = 1024) -> None:
        self.program = list(map(lambda t: Opcode(t[1]), sorted(factor(program))))
        self.memory = [0]*memory_size
        self.loop_stack = []
        self.pointer = 0
        self.program_counter = 0

    def run(self) -> None:
        while self.program_counter < len(self.program):
            match self.program[self.program_counter]:
                case Opcode.INC_PTR: self.pointer = (self.pointer + 1) % len(self.memory)
                case Opcode.DEC_PTR: self.pointer = (self.pointer - 1) % len(self.memory)
                case Opcode.ADD: self.memory[self.pointer] += 1
                case Opcode.SUB: self.memory[self.pointer] -= 1
                case Opcode.LOOP_ST:
                    if self.memory[self.pointer] == 0:
                        self.__level = 1
                        while self.__level > 0:
                            self.program_counter += 1
                            # print(self.program_counter, self.program[self.program_counter], self.__level, len(self.program))
                            if self.program[self.program_counter] == Opcode.LOOP_ST:
                                self.__level += 1
                            elif self.program[self.program_counter] == Opcode.LOOP_EN:
                                self.__level -= 1
                    else:
                        self.loop_stack.append(self.program_counter)
                case Opcode.LOOP_EN:
                    if self.memory[self.pointer] != 0:
                        self.program_counter = self.loop_stack[-1]
                    else:
                        self.loop_stack.pop()
                case Opcode.GETCH: pass
                case Opcode.PUTCH: print(chr(self.memory[self.pointer]), end='')
            self.program_counter += 1

set_int_max_str_digits(1_000_000_000)

num = 0

with open(r'c:\Users\PC\Desktop\pnpl\src\num.txt') as file:
    for n in file.read():
        num = num*10 + int(n)
    # print(num)

PNPL(num, memory_size=4096).run()