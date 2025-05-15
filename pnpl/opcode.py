"""This module contains the `Opcode` class, which aims to abstract all possible PNPL operations in a single enum."""
from enum import Enum

class Opcode(Enum):
    """An enum that groups all PNPL instructions."""

    INC_PTR = 1
    """Moves the memory pointer to the right."""
    DEC_PTR = 2
    """Moves the memory pointer to the left."""
    ADD     = 3
    """Increases the memory cell at the pointer by one."""
    SUB     = 4
    """Decreases the memory cell at the pointer by one."""
    LOOP_ST = 5
    """Jumps past the matching `LOOP_EN` if the cell at the pointer is 0."""
    LOOP_EN = 6
    """Jumps back to the matching `LOOP_ST` if the cell at the pointer is nonzero."""
    GETCH   = 7
    """Inputs a character and stores it in the cell at the pointer."""
    PUTCH   = 8
    """Outputs the character encoded by the cell at the pointer."""

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
        """Convert the instruction to its Brainfuck analog."""
        match self:
            case Opcode.INC_PTR: return '>'
            case Opcode.DEC_PTR: return '<'
            case Opcode.ADD:     return '+'
            case Opcode.SUB:     return '-'
            case Opcode.LOOP_ST: return '['
            case Opcode.LOOP_EN: return ']'
            case Opcode.GETCH:   return ','
            case Opcode.PUTCH:   return '.'