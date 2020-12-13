def part_one() -> None:
    with open("input_data.txt") as fh:
        values = [int(line.strip()) for line in fh]
    values.append(0)
    values.append(max(values) + 3)
    values = sorted(values)
    result = []
    for i in range(len(values) - 1):
        result.append(values[i + 1] - values[i])
    one_jolt = sum([1 for val in result if val == 1])
    three_jolt = sum([1 for val in result if val == 3])
    print(f"Result for part one is {one_jolt * three_jolt}")


def part_two() -> None:
    with open("input_data.txt") as fh:
        values = [int(line.strip()) for line in fh]

    max_value = max(values) + 3
    values.append(max_value)
    values = sorted(values)

    paths = {0: 1}
    for value in values:
        paths[value] = paths.get(value - 3, 0) + paths.get(value - 2, 0) + paths.get(value - 1, 0)

    print(f"Result for part two is {paths[max_value]}")


def main():
    part_one()
    part_two()


if __name__ == '__main__':
    main()
