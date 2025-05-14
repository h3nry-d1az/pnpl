""".. include:: ../README.md"""
from . import opcode
from . import primality

from typing import List

from .opcode import Opcode
from .primality import factor

class PNPL:
    """This class represents a PNPL interpreter, identical in functionality to any Brainfuck one but with prime numbers as instructions."""
    memory: List[int]
    pointer: int = 0
    program: List[Opcode]
    program_counter: int = 0
    __loop_stack: List[int]
    __level: int = 0

    def __init__(self, program: int, memory_size: int = 1024) -> None:
        """Creates a PNPL machine from its input (integer) program and the size of its memory array (by default $1024$)."""
        self.program = list(map(lambda t: Opcode(t[1]), sorted(factor(program))))
        self.memory = [0]*memory_size
        self.pointer = 0
        self.program_counter = 0
        self.__loop_stack = []

    @classmethod
    def from_file(cls, path: str, memory_size: int = 1024):
        """Works identically to the main constructor but the path of the program file must be provided instead of its literal value."""
        program = 0
        with open(path) as file:
            for char in file.read():
                try: program = 10*program + int(char)
                except ValueError: continue
        return cls(program, memory_size)

    def load(self, program: int) -> None:
        """Load a program into the machine."""
        self.program = list(map(lambda t: Opcode(t[1]), sorted(factor(program))))
        self.program_counter = 0

    def run(self) -> None:
        """Executes the program stored in memory."""
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
                            if self.program[self.program_counter] == Opcode.LOOP_ST:
                                self.__level += 1
                            elif self.program[self.program_counter] == Opcode.LOOP_EN:
                                self.__level -= 1
                    else:
                        self.__loop_stack.append(self.program_counter)
                case Opcode.LOOP_EN:
                    if self.memory[self.pointer] != 0:
                        self.program_counter = self.__loop_stack[-1]
                    else:
                        self.__loop_stack.pop()
                case Opcode.GETCH: pass
                case Opcode.PUTCH: print(chr(self.memory[self.pointer]), end='')
            self.program_counter += 1


    def reset(self, memory_size: int = 1024) -> None:
        """Reset the PNPL interpreter's program and memory."""
        self.program = []
        self.program_counter = 0
        self.memory = [0]*memory_size
        self.pointer = 0