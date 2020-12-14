from typing import List
import itertools


def _mask_number(number: int, add: int, remove: int):
    number = number | add
    number = number & ~remove
    return number


def part_one() -> None:
    memory = {}
    mask_add = 0
    mask_remove = 0
    with open("input_data.txt") as fh:
        for line in fh:
            line = line.strip()
            parts = line.split(" = ")
            if parts[0] == "mask":
                mask_add = int("".join(['1' if letter == '1' else '0' for letter in parts[1]]), 2)
                mask_remove = int("".join(['1' if letter == '0' else '0' for letter in parts[1]]), 2)
            else:
                memory[int(parts[0][4:-1])] = _mask_number(int(parts[1]), mask_add, mask_remove)
    print(f"Result for part two is {sum(memory.values())}")


def _generate_types(length) -> List[List[str]]:
    strings = ['0', '1']
    result = []
    for item in itertools.product(strings, repeat=length):
        result.append(list(item))
    return result


def _get_mask_val(mask: str, seq: List[str]) -> int:
    result = ''
    current = 0
    for letter in mask:
        if letter == 'X':
            result += seq[current]
            current += 1
        else:
            result += letter
    return int(result, 2)


def _get_all_positions(value: int, mask: str) -> List[int]:
    result = []
    value &= int(''.join(['1' if letter == '0' else '0' for letter in mask]), 2)
    count = sum([1 for letter in mask if letter == 'X'])
    for seq in _generate_types(count):
        result.append(value | _get_mask_val(mask, seq))
    return list(set(result))


def part_two() -> None:
    memory = {}
    mask = '0' * 36
    with open("input_data.txt") as fh:
        for line in fh:
            line = line.rstrip()
            parts = line.split(" = ")
            if parts[0] == "mask":
                mask = parts[1]
            else:
                for position in _get_all_positions(int(parts[0][4:-1]), mask):
                    memory[position] = int(parts[1])
    print(f"Result for part two is {sum(memory.values())}")


def main():
    part_one()
    part_two()


if __name__ == '__main__':
    main()
