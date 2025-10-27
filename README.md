# postfix-calculator
This project implements a stack-based evaluator for postfix (Reverse Polish Notation) expressions in Python.

## Features
- Stack class (push, pop, peek, size).
- Evaluates standard postfix math expressions.
- Supports multi-digit numbers:
  - `"12 4 + 2 *"` → `32`
- Supports operators:
  - Addition `+`
  - Subtraction `-`
  - Multiplication `*`
  - Division `/`
  - Modulus `%`
  - Exponent `^`
- Supports unary math functions:
  - `sqrt x` (square root)

## Examples

```python
from postfix_eval import postfix_eval

print(postfix_eval("3 4 + 2 *"))            # 14
print(postfix_eval("12 4 + 2 *"))           # 32
print(postfix_eval("3 4 + 2 ^"))            # 49
print(postfix_eval("5 1 2 + 4 * + 3 -"))    # 14
print(postfix_eval("9 sqrt 2 ^"))           # 9.0
