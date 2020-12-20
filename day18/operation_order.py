from __future__ import annotations
from typing import Callable


def recursive_calculator(line: str, f: Callable[[str], int]) -> int:
    if '(' not in line:
        return f(line)

    result = {}
    stack = []

    for index, char in enumerate(line):
        if char == '(':
            stack.append(index)
        elif char == ')':
            result[stack.pop()] = index

    k, v = next(iter(result.items()))
    expr = str(recursive_calculator(line[k + 1: v], f))
    return recursive_calculator(line[:k] + expr + line[v + 1:], f)


def eval_one(expr: str) -> int:
    parts = expr.split()
    result = 0
    operator = '+'

    for c in parts:
        if c in {'+', '*'}:
            operator = c
        elif operator == '+':
            result += int(c)
        else:
            result *= int(c)

    return result


def eval_two(expr: str) -> int:
    parts = expr.split('*')
    result = 1

    for part in parts:
        result *= eval_one(part)

    return result


def part_one(input_path: str) -> None:
    with open(input_path) as fh:
        lines = [line.rstrip() for line in fh]

    total = sum(recursive_calculator(line, eval_one) for line in lines)

    print(f'Result for part one is {total}')


def part_two(input_path: str) -> None:
    with open(input_path) as fh:
        lines = [line.rstrip() for line in fh]

    total = sum(recursive_calculator(line, eval_two) for line in lines)

    print(f'Result for part two is {total}')


def main():
    source = "input_data.txt"
    part_one(source)
    part_two(source)


if __name__ == '__main__':
    main()