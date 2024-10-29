
# 0x02. Minimum Operations

## Description

This project involves solving the problem of calculating the minimum number of operations needed to result in exactly `n` copies of the character 'H' in a text editor. The only available operations are:

1. **Copy All**: Copy all the characters in the current text.
2. **Paste**: Paste the characters that were last copied.

The task is to determine the minimum number of steps to achieve exactly `n` copies of 'H', starting with just one 'H' in the editor.

## Learning Objectives

- Understand how to approach algorithmic problems involving optimal sequences of operations.
- Learn to solve problems using factors and prime factorization.

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`.
- The code should be compiled and tested on Ubuntu 20.04 LTS using `python3`.
- Your code should use the PEP8 style guide (version 2.7).

## Tasks

### Task 0: Minimum Operations

**File**: `0-minoperations.py`

**Description**:
- Write a method that calculates the fewest number of operations needed to get exactly `n` copies of the character 'H' in a text editor.

**Prototype**:
```python
def minOperations(n: int) -> int:
```

**Parameters**:
- `n` (integer): The number of 'H' characters needed.

**Return Value**:
- The function should return an integer, representing the minimum number of operations required to achieve `n` copies.
- If `n` is impossible to achieve, return `0`.

### Example

```python
>>> minOperations(4)
4

>>> minOperations(12)
7
```

### Explanation

For `n = 4`:
- Copy All, Paste, Paste, Paste => 4 operations.

For `n = 12`:
- Copy All, Paste (2), Copy All, Paste (4), Paste (6), Copy All, Paste (12) => 7 operations.

## Algorithmic Approach

To find the minimum number of operations:
- Factorize `n` and use its prime factors to determine the sequence of "Copy All" and "Paste" operations required to reach `n` characters.
- The number of operations is equal to the sum of the prime factors of `n`.
