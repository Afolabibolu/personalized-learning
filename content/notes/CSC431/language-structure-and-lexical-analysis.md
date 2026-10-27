# Programming Language Structure and Lexical Analysis

## Structure of programming languages

The **syntax** of a language is the rule that says whether a string of characters is a valid program; its **semantics** are the rules that attach meaning to valid programs. Every language has its own **character set**;

**Tokens** are combinations of symbols that make up the language: constants (1, 5E6), identifiers (name, speed), operator symbols (+, <=), keywords (Pascal has 35) and punctuation symbols. Tokens can be defined in **BNF** (Backus–Naur Form), for example <integer> ::= <sign><digit>{<digit>} and <digit> ::= 0 | 1 | ... | 9.

Other elements a compiler designer must decide:

- **Data elements:** numbers, Boolean, character data, pointers and structures such as arrays and records.
- **Binding:** associating an element with a property such as a type, storage or value. Some bindings happen when the program is written (int x), some at compile time (machine instructions) and some at run time (storage for local variables).
- **Identifiers:** names of data objects; their most important attribute is the data type.
- **Operators:** arithmetic, relational, assignment, logical and string operators.
- **Coercion:** automatic conversion of a value of one type to another, so that mixed-type expressions give a definite result.
- **Storage management:** the size of each primitive type (in Java, int and float 32 bits, long and double 64 bits) and the policy, **static** or **dynamic**, such as stack allocation.
- **Parameter transmission:** **by reference** (two-way communication between actual and formal parameters) or **by value** (no value returned to the caller).

## Lexical analysis

The **scanner** (lexical analyser) reads the source program character by character and separates it into **tokens** or lexemes. Regular expressions describe tokens because lexical rules are simple, regular expressions are concise, and more efficient scanners can be generated from them than from grammars.

The scanner's tasks are to break the source program into tokens, produce tables for them, and present the program in a manageable internal form. It needs the language rules, the source program, tables of tokens and the terminal symbols.

Routines used to implement a scanner include:

1. **Get_Next_Char()**, which reads the next character and delivers the next symbol.
2. A routine to check whether a symbol is already in the symbol table.
3. A routine to enter the symbol in the appropriate table.
4. A routine to find the class of a symbol, such as integer, real or array.
5. **Mark**, which reports errors with their position.

The scanner skips blanks, line ends and comments; recognises reserved words, identifiers (letters and digits starting with a letter), numbers and two-character symbols such as := and <=; and returns **null** for an illegal character and **eof** at the end. Symbols are mapped to integers, for example "print" = 5.

Source: CSC 431 Compiler Construction.pdf (Ibadan Distance Learning course material), Study Sessions 6 and 7
