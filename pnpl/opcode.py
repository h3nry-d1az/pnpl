"""This module contains the `Opcode` class, which aims to abstract all possible PNPL operations in a single enum."""
from enum import Enum

class Opcode(Enum):
    """An enum that groups all PNPL instructions."""
    INC_PTR = 1
    DEC_PTR = 2
    ADD     = 3
    SUB     = 4
    LOOP_ST = 5
    LOOP_EN = 6
    GETCH   = 7
    PUTCH   = 8

    @classmethod
    def from_bf(cls, char: str):
        """Create an `Opcode` instance from its equivalent Brainfuck symbol."""
        match char:
            case '>': return cls(1)
            case '<': return cls(2)
            case '+': return cls(3)
            case '-': return cls(4)
            case '[': return cls(5)
            case ']': return cls(6)
            case ',': return cls(7)
            case '.': return cls(8)
            case _:   return None

    @property
    def as_bf(self) -> str:
        """Return the analog Brainfuck operation."""
        match self:
            case Opcode.INC_PTR: return '>'
            case Opcode.DEC_PTR: return '<'
            case Opcode.ADD:     return '+'
            case Opcode.SUB:     return '-'
            case Opcode.LOOP_ST: return '['
            case Opcode.LOOP_EN: return ']'
            case Opcode.GETCH:   return ','
            case Opcode.PUTCH:   return '.'