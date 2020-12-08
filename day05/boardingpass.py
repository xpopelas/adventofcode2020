from typing import List


class BoardingPass:
    id: int

    def __init__(self, pass_combo: str):
        self.id = self.__calculate_id(pass_combo)

    @staticmethod
    def __calculate_id(pass_combo: str) -> int:
        result = 0
        for letter in pass_combo:
            result <<= 1
            if letter in ['R', 'B']:
                result += 1
        return result

    def row(self) -> int:
        return self.id // 8

    def col(self) -> int:
        return self.id % 8


def get_boarding_passes(input_path: str) -> List[BoardingPass]:
    result = []
    with open(input_path, 'r') as fh:
        for line in fh:
            result.append(BoardingPass(line.strip()))
    return result


def part_one(passes: List[BoardingPass]) -> None:
    print(f"Highest id out of all is {max([board.id for board in passes])}")


def part_two(passes: List[BoardingPass]) -> None:
    ids = sorted([boarding_pass.id for boarding_pass in passes])
    for pass_id in range(min(ids), max(ids)):
        if pass_id - 1 in ids and pass_id not in ids and pass_id + 1 in ids:
            print(f"Your boarding pass id is {pass_id}")


def main():
    passes = get_boarding_passes("input_data.txt")
    part_one(passes)
    part_two(passes)


if __name__ == '__main__':
    main()
