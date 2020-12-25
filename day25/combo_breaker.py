from sympy.ntheory.residue_ntheory import discrete_log
from typing import Tuple


def part_one(code: Tuple[int, int]) -> None:
    subject_number = 7
    cycle = 20201227
    result = pow(code[1], discrete_log(cycle, code[0], subject_number), cycle)

    print(f"Result for part one is {result}")


def part_two() -> None:
    print("There's not part two for this day :) Happy holidays")


def main() -> None:
    source = "input_data.txt"
    temp = open(source).read().rstrip().splitlines()
    card, door = int(temp[0]), int(temp[1])
    part_one((card, door))
    part_two()


if __name__ == '__main__':
    main()
