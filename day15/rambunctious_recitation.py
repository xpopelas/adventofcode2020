from typing import List, Tuple


def _recitation(index: dict, order: List[int]) -> None:
    value = order[-1]
    if value not in index or len(index[value]) == 1:
        to_say = 0
    else:
        to_say = index[value][-1] - index[value][-2]

    if to_say in index:
        index[to_say].append(len(order))
    else:
        index[to_say] = [len(order)]

    order.append(to_say)


def _build_index_and_order(input_path: str) -> Tuple[dict, List[int]]:
    index = {}
    order = []
    with open("input_data.txt") as fh:
        to_add = [int(x) for x in fh.readline().rstrip().split(',')]

    count = 0
    for number in to_add:
        if number not in index:
            index[number] = [count]
        else:
            index[number].append(count)
        order.append(number)
        count += 1

    return index, order


def part_one(input_path: str) -> Tuple[dict, List[int]]:
    index, order = _build_index_and_order(input_path)

    while len(order) != 2020:
        _recitation(index, order)

    print(f"Result for part one is {order[-1]}")

    return index, order


def part_two(index: dict, order: List[int]) -> None:
    print("This solution is rather slow, this will take a while...")

    while len(order) != 30000000:
        _recitation(index, order)

    print(f"Result for part two is {order[-1]}")


def main() -> None:
    index, order = part_one("input_data.txt")
    part_two(index, order)


if __name__ == '__main__':
    main()

