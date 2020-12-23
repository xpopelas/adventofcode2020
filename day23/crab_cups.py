from typing import List
from array import array


class CrabCups:
    cups: List[int]

    def __init__(self, line: str):
        self.cups = [int(c) for c in line]
        self.array = None

    def part_init(self, part: int):
        if part == 1:
            self.array = array('I', [0 for _ in range(9)])
            for i, cup in enumerate(self.cups):
                self.array[cup - 1] = self.cups[(i + 1) % len(self.cups)] - 1
        elif part == 2:
            self.array = array('I', range(1, 1000000 + 1))
            for i, cup in enumerate(self.cups):
                self.array[cup - 1] = self.cups[i + 1] - 1 if i + 1 < len(self.cups) else 9

    def game(self, destination):
        first = self.array[destination]
        second = self.array[first]
        third = self.array[second]
        result = self.array[third]
        
        temp = destination - 1 if destination > 0 else len(self.array) - 1
        while temp in (first, second, third):
            temp = temp - 1 if temp > 0 else len(self.array) - 1

        u = self.array[temp]
        self.array[destination] = result
        self.array[temp] = first
        self.array[third] = u
        return result


def part_one(line: str) -> None:
    game = CrabCups(line)
    game.part_init(1)
    current = game.cups[0] - 1
    for _ in range(100):
        current = game.game(current)
    current, result = 0, 0
    while True:
        current = game.array[current]
        if not current:
            print(f'Result for part one is {result}')
            return
        result = 10 * result + current + 1


def part_two(line: str) -> None:
    print('Part 2 will take a second...')
    game = CrabCups(line)
    game.part_init(2)
    game.array[-1] = game.cups[0] - 1
    x = game.cups[0] - 1
    for _ in range(10000000):
        x = game.game(x)
    result = (game.array[0] + 1) * (game.array[game.array[0]] + 1)
    print(f'Result for part two is {result}')


def main() -> None:
    with open("input_data.txt") as fh:
        line = fh.readline().rstrip()
    part_one(line)
    part_two(line)


if __name__ == '__main__':
    main()
