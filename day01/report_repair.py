from typing import List, Tuple


def find_three_sum(input_set: List[int], to_sum: int) -> Tuple[int, int, int]:
    for i in range(len(input_set)):
        for j in range(i + 1, len(input_set)):
            for k in range(j + 1, len(input_set)):
                if input_set[i] + input_set[j] + input_set[k] == to_sum:
                    return input_set[i], input_set[j], input_set[k]
    return 0, 0, 0


def find_to_sum(input_set: List[int], to_sum: int) -> Tuple[int, int]:
    for i in range(len(input_set)):
        for j in range(i + 1, len(input_set)):
            if input_set[i] + input_set[j] == to_sum:
                return input_set[i], input_set[j]
    return 0, 0


def input_file_to_list(input_path: str) -> List[int]:
    result = []
    with open(input_path, "r") as file_handler:
        for file_line in file_handler:
            result.append(int(file_line))
    return result


def part_one(input_list: List[int]) -> None:
    two_numbers = find_to_sum(input_list, 2020)
    print(f"The two numbers are {two_numbers[0]} and {two_numbers[1]}")
    print(f"Answer to part1 is {two_numbers[0] * two_numbers[1]}")


def part_two(input_list: List[int]) -> None:
    three_numbers = find_three_sum(input_list, 2020)
    print(f"The three numbers are {three_numbers[0]}, {three_numbers[1]} and {three_numbers[2]}")
    print(f"Answer to part2 is {three_numbers[0] * three_numbers[1] * three_numbers[2]}")


def main() -> None:
    input_list = input_file_to_list("input_data.txt")
    part_one(input_list)
    part_two(input_list)


if __name__ == '__main__':
    main()
