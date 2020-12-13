from typing import List, Tuple


def check_last(values: List[int], last_index: int = -1) -> bool:
    last = values[last_index]
    for i in range(25):
        for j in range(i + 1, 25):
            first = values[last_index - 25 + i]
            second = values[last_index - 25 + j]
            if first != second and first + second == last:
                return True
    return False


def part_one(values: List[int]) -> int:
    for i in range(25, len(values)):
        if not check_last(values, i):
            print(f"Result for part one is {values[i]}")
            return values[i]


def find_sum(values: List[int], to_sum: int) -> Tuple[int, int]:
    l_index = 0
    r_index = 1
    val = values[0]

    while r_index < len(values):
        if val < to_sum:
            r_index += 1
            val = sum(values[l_index:r_index])
        elif val > to_sum:
            l_index += 1
            val = sum(values[l_index:r_index])
        else:
            return min(values[l_index:r_index]), max(values[l_index:r_index])
    return 0, 0


def part_two(values: List[int], value: int) -> None:
    a, b = find_sum(values, value)
    print(f"Result for part two is {a + b}")


def main():
    with open("input_data.txt") as fh:
        values = [int(line.rstrip()) for line in fh]
    value = part_one(values)
    part_two(values, value)


if __name__ == '__main__':
    main()
