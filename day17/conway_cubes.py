from typing import Tuple, Set


class ConwayCube:
    active_values: Set[Tuple[int, int, int, int]]

    def __init__(self, input_path: str):
        self.active_values = set()
        z = 0
        w = 0
        with open(input_path) as fh:
            y = 0
            for line in fh:
                line = line.rstrip()
                for x in range(len(line)):
                    if line[x] == '#':
                        self.active_values.add((x, y, z, w))
                y += 1

    def is_active(self, x: int, y: int, z: int, w: int) -> bool:
        return (x, y, z, w) in self.active_values

    def neighbours_3d(self, x: int, y: int, z: int) -> int:
        result = 0
        for i in [x - 1, x, x + 1]:
            for j in [y - 1, y, y + 1]:
                for k in [z - 1, z, z + 1]:
                    if i == x and j == y and k == z:
                        continue

                    if self.is_active(i, j, k, 0):
                        result += 1

        return result

    def neighbours_4d(self, x: int, y: int, z: int, w: int) -> int:
        result = 0
        for i in [x - 1, x, x + 1]:
            for j in [y - 1, y, y + 1]:
                for k in [z - 1, z, z + 1]:
                    for l in [w - 1, w, w + 1]:
                        if i == x and j == y and k == z and l == w:
                            continue

                        if self.is_active(i, j, k, l):
                            result += 1

        return result

    def generation_step_3d(self):
        new_values = set()
        for a, b, c, _ in self.active_values:
            for x in [a - 1, a, a + 1]:
                for y in [b - 1, b, b + 1]:
                    for z in [c - 1, c, c + 1]:
                        neighbours = self.neighbours_3d(x, y, z)
                        if self.is_active(x, y, z, 0) and neighbours in {2, 3}:
                            new_values.add((x, y, z, 0))
                        if not self.is_active(x, y, z, 0) and neighbours == 3:
                            new_values.add((x, y, z, 0))

        self.active_values = new_values

    def generation_step_4d(self):
        new_values = set()
        for a, b, c, d in self.active_values:
            for x in [a - 1, a, a + 1]:
                for y in [b - 1, b, b + 1]:
                    for z in [c - 1, c, c + 1]:
                        for w in [d - 1, d, d + 1]:
                            neighbours = self.neighbours_4d(x, y, z, w)
                            if self.is_active(x, y, z, w) and neighbours in {2, 3}:
                                new_values.add((x, y, z, w))
                            if not self.is_active(x, y, z, w) and neighbours == 3:
                                new_values.add((x, y, z, w))

        self.active_values = new_values

    def total(self) -> int:
        return len(self.active_values)


def part_one(input_path: str) -> None:
    cube = ConwayCube(input_path)
    for _ in range(6):
        cube.generation_step_3d()

    print(f"Result for part one: {cube.total()}")


def part_two(input_path: str) -> None:
    print("The solution for part 2 is rather slow and will take some time...")
    cube = ConwayCube(input_path)
    for _ in range(6):
        cube.generation_step_4d()

    print(f"Result for part two: {cube.total()}")


def main():
    input_path = "input_data.txt"
    part_one(input_path)
    part_two(input_path)


if __name__ == '__main__':
    main()
