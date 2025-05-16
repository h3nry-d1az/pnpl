# Prime Number Programming Language
**Prime Number Programming Language (PNPL)** is a Brainfuck-equivalent esoteric language that revolves around prime numbers and the uniqueness of their products.

## Installation
This repository maintains the code for the official PNPL implementation. It contains an interpreter made in Python, which is exposed as a CLI with a built-in REPL.

The latest version may be installed by executing the following command:
```
pip install git+https://github.com/h3nry-d1az/pnpl
```

## CLI Usage
All the possible modes and flags admitted by the PNPL CLI can be listed by executing `pnpl -h` after the installation process is completed, which prints the following screen:
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
```

## Language Overview
In PNPL, all valid programs are natural numbers, whose behavior is determined by the fundamental theorem of arithmetic (FTA henceforth).

Recall that, because of FTA, every positive integer can be expressed as a singular product of distinct prime numbers raised to integer exponents; since the set of prime numbers is totally ordered, the first prime in its factorization denotes the first instruction, and its exponent the operation to be performed.

There are a total of 8 possible commands in PNPL; therefore, any correct PNPL program $P$ is of the form
<div align="center">

  $$P=2^{\alpha_1} 3^{\alpha_2} 5^{\alpha_3} \cdots {p_n}^{\alpha_n},\quad\text{where}\quad\alpha_i\in\\{0,1,2,3,4,5,6,7,8\\}$$

</div>

### Command List
PNPL's operations have been deliberately chosen in order to be computationally equivalent to Brainfuck:

<table><thead>
  <tr>
    <th>Exponent</th>
    <th>Brainfuck cognate</th>
    <th>Description</th>
  </tr></thead>
<tbody>
  <tr>
    <td>0</td>
    <td></td>
    <td>Do nothing.</td>
  </tr>
  <tr>
    <td>1</td>
    <td><code>&gt;</code></td>
    <td>Moves the memory pointer to the right.</td>
  </tr>
  <tr>
    <td>2</td>
    <td><code>&lt;</code></td>
    <td>Moves the memory pointer to the left.</td>
  </tr>
  <tr>
    <td>3</td>
    <td><code>+</code></td>
    <td>Increases the memory cell at the pointer by one.</td>
  </tr>
  <tr>
    <td>4</td>
    <td><code>-</code></td>
    <td>Increases the memory cell at the pointer by one.</td>
  </tr>
  <tr>
    <td>5</td>
    <td><code>[</code></td>
    <td>Jumps past the matching loop ending (exponent 6) if the cell at the pointer is 0.</td>
  </tr>
  <tr>
    <td>6</td>
    <td><code>]</code></td>
    <td>Jumps back to the matching loop start (exponent 5) if the cell at the pointer is nonzero.</td>
  </tr>
  <tr>
    <td>7</td>
    <td><code>,</code></td>
    <td>Inputs a character and stores it in the cell at the pointer.</td>
  </tr>
  <tr>
    <td>8</td>
    <td><code>.</code></td>
    <td>Outputs the character encoded by the cell at the pointer.</td>
  </tr>
</tbody></table>
The isomorphism between Brainfuck and PNPL programs directly implies the Turing completeness of the latter.

## Example Programs

Because of the parallelism described above, translating Brainfuck programs directly to PNPL turns out to be fairly straightforward. Thus, in the [`samples`](samples/) directory are listed a few of these compilations:

* [`hello.pn`](samples/hello.pn): This program outputs "Hello World!".
* [`pi.pn`](samples/pi.pn): Computes $\pi$ and prints an approximation to 14 decimal places.
* [`sierpinski.pn`](samples/sierpinski.pn): Shows an ASCII representation of the fifth iteration of the Sierpinski triangle.
* [`squares.pn`](samples/squares.pn): Outputs the square numbers from 0 to 10000.

## Possible Modifications

The instruction set of this language may be expanded even further to include multiple operands for every command. This can be achieved by considering each instruction a "program" on its own, that is:
<div align="center">

$$i_n = 2^{\omega_n}3^{a_{n1}} 5^{a_{n2}}\cdots {p_k}^{a_{n(k-1)}}$$

</div>

Here, $i_n$ denotes the $n$ th instruction, $\omega_n$ its opcode and $a_{nk}$ its $k$ th argument. Overall, an extended PNPL program would be of the form:
<div align="center">

  $$P=2^{i_1} 3^{i_2} 5^{i_3} \cdots {p_n}^{i_n} = 2^{2^{\omega_1}3^{a_{11}} 5^{a_{12}}\cdots {p_k}^{a_{1(k-1)}}}\cdots {p_k}^{2^{\omega_k}3^{a_{k1}} 5^{a_{k2}}\cdots {p_j}^{a_{k(j-1)}}}$$

</div>

This architecture is indeed more versatile in the theoretical frame, yet in practice programs scale much more rapidly, in such a manner that turns out to be unfeasible to handle in reasonable time and memory constraints.

## History

Originally, this language was named pirho ($\Pi_\rho$) and was published as my final project for the ESTALMAT program. Although its foundations in the FTA were the same, its syntax was highly troublesome, thus, PNPL is meant to be a revised version of the concept.

## External resources
* [Esolang's wiki page for PNPL.](https://esolangs.org/wiki/PNPL)
* [Blog post on the history of the language and its announcement.](https://h3nry-d1az.github.io/posts/2025/pnpl/)
