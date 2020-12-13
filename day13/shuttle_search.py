from typing import List


def modulo_of(n: int, values: List[int]) -> int:
    for value in values:
        if n % value == 0:
            return value
    return 0


def part_one() -> None:
    with open("input_data.txt") as fh:
        timestamp = int(fh.readline().rstrip())
        times = [int(part) for part in fh.readline().rstrip().split(',') if part != 'x']

    result = 0
    while modulo_of(timestamp, times) == 0:
        timestamp += 1
        result += 1
    print(f"Result for part one is {result * modulo_of(timestamp, times)}")


def part_two() -> None:
    with open("input_data.txt") as fh:
        fh.readline()  # the first line is arbitrary
        info = fh.readline().rstrip().split(',')

    timestamp = 0
    product = 1
    index = -1

    for letter in info:
        index += 1
        if letter == 'x':
            continue
        while (timestamp + index) % int(letter) != 0:
            timestamp += product
        product *= int(letter)
    print(f"Result for part two is {timestamp}")


def main() -> None:
    part_one()
    part_two()


if __name__ == '__main__':
    main()
