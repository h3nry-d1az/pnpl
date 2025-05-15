"""A command line interface for PNPL, which includes the following features (see `pnpl -h`):
```
usage: pnpl [-h] [-e program] [-r file_name] [--repl] [-b2p input_file output_file] [-p2b input_file output_file] [-m size]

Prime Number Programming Language, an esoteric language based on the fundamental theorem of arithmetic.

options:
  -h, --help            show this help message and exit
  -e, --eval program    execute the program provided as an argument.
  -r, --run file_name   read and execute the program stored in the input file.
  --repl                start the PNPL REPL.
  -b2p, --bf2pnpl input_file output_file
                        convert a Brainfuck program to PNPL.
  -p2b, --pnpl2bf input_file output_file
                        convert a PNPL program to Brainfuck.
  -m, --memory size     set the size of the memory array.
```"""
from . import PNPL
from .opcode import Opcode
from .primality import factor, next_prime, reset_prime_counter

import argparse
from sys import set_int_max_str_digits

def repl(memory: int) -> None:
    """REPL entry point."""
    print('Welcome to the PNPL sandbox! Here you can execute your programs interactively.\n'
          'Type `help` to see all the available commands.')
    n = 1
    memsize = memory
    machine = PNPL(2)
    machine.reset(memsize)
    while True:
        instruction = input(f'\n[{n}] ').strip()
        if instruction == 'help':
            print('\nWelcome to the PNPL sandbox! Here you can execute your programs interactively.\n'
                  'Type any valid program and the interpreter will execute it, although it will not clean the memory tape afterwards.\n'
                  'There are a few special commands for debugging purposes as well:\n',
                  "* reset: Deliberately resets the machine's memory, pointer and program counter.\n"
                  " * dump: Prints the machine's memory tape, but does not erase it.\n"
                  " * mem (size): Change the size of the memory to the provided integer, truncating or extending the previous tape.\n"
                  " * bf (program): Translate, print, and then execute a Brainfuck program.\n"
                  " * exit: Exits the REPL.")
        elif instruction == 'exit': return
        elif instruction == 'reset': machine.reset(memsize)
        elif instruction == 'dump': print(*machine.memory)
        elif len(instruction) >= 3 and instruction[0:3] == 'mem':
            try:
                memsize = int(instruction[3:])
                newmem = [0]*memsize
                for i, e in enumerate(machine.memory):
                    try: newmem[i] = e
                    except IndexError: break
                machine.memory = newmem
            except ValueError: print('Invalid memory size, not an integer.')
            except IndexError: print('The `mem` command requires a memory size as argument.')
        elif instruction[0:2] == 'bf':
            try:
                p = bf2pnpl(instruction[3:])
                print(p)
                machine.load(p)
                machine.run()
            except ValueError: print('The `bf` command requires a Brainfuck program as argument.')
        elif instruction == 'doggo': print('\nA dog walked into a tavern and said, "I can\'t see a thing. I\'ll open this one."\n'
                                           'A project by Henry Díaz Bordón, based on the now-dead pirho language.')
        elif instruction == '': continue
        else:
            try: machine.load(int(instruction)); machine.run()
            except ValueError: print('Invalid PNPL program, not an integer.')
        n += 1


def bf2pnpl(program: str) -> int:
    """Convert a Brainfuck program to PNPL."""
    reset_prime_counter()
    n = 1
    for opcode in program:
        exponent = Opcode.from_bf(opcode) 
        n = n * next_prime()**(exponent.value) if exponent else n
    return n

def pnpl2bf(program: int) -> str:
    """Convert a PNPL program to Brainfuck."""
    output = ""
    for opcode in map(lambda t: Opcode(t[1]), sorted(factor(program))):
        output += opcode.as_bf if opcode else ''
    return output

def main() -> None:
    """Entry point of the CLI."""
    set_int_max_str_digits(1<<31-1)

    cli = argparse.ArgumentParser(description='Prime Number Programming Language, an esoteric language based on the fundamental theorem of arithmetic.')

    cli.add_argument("-e", "--eval", type=int, nargs=1, metavar='program', default=None, help="execute the program provided as an argument.")
    cli.add_argument("-r", "--run", type=str, nargs=1, metavar='file_name', default=None, help="read and execute the program stored in the input file.")
    cli.add_argument("--repl", action='store_true', help="start the PNPL REPL.")
    cli.add_argument("-b2p", "--bf2pnpl", type=str, nargs=2, metavar=('input_file', 'output_file'), default=None, help="convert a Brainfuck program to PNPL.")
    cli.add_argument("-p2b", "--pnpl2bf", type=str, nargs=2, metavar=('input_file', 'output_file'), default=None, help="convert a PNPL program to Brainfuck.")

    cli.add_argument("-m", "--memory", type=int, nargs=1, metavar='size', default=1024, help="set the size of the memory array.")

    args = cli.parse_args()

    machine_memory = args.memory[0]

    if args.eval: PNPL(args.eval[0], machine_memory).run()
    elif args.run: PNPL.from_file(args.run[0], machine_memory).run()
    elif args.repl: repl(machine_memory)
    elif args.bf2pnpl: open(args.bf2pnpl[1], 'w').write(str(bf2pnpl(open(args.bf2pnpl[0]).read())))
    elif args.pnpl2bf: open(args.pnpl2bf[1], 'w').write(pnpl2bf(int(open(args.pnpl2bf[0]).read())))


if __name__ == '__main__': main()