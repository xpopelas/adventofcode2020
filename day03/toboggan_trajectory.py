from typing import List


class Plane2D:
    gameplan: List[List[str]]

    def __init__(self, input_path: str = None):
        self.gameplan = [[]]
        if input_path is not None:
            self.__from_file(input_path)

    def width(self) -> int:
        return len(self.gameplan[0])

    def height(self) -> int:
        return len(self.gameplan)

    def at(self, x: int, y: int) -> str:
        return self.gameplan[y % self.height()][x % self.width()]

    def __from_file(self, input_path: str) -> None:
        self.gameplan = []
        with open(input_path, 'r') as fh:
            for line in fh:
                self.gameplan.append([i for i in line.strip()])

    def traverse(self, x_inc, y_inc, length, x=0, y=0, search='#') -> int:
        result = 0
        for _ in range(length):
            x += x_inc
            y += y_inc
            if self.at(x, y) == search:
                result += 1
        return result


def part_one(my_plane: Plane2D) -> None:
    print(f"There are total of {my_plane.traverse(3, 1, my_plane.height() - 1)} trees in sight")


def part_two(my_plane: Plane2D) -> None:
    result = 1
    for x, y in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        result *= my_plane.traverse(x, y, int((my_plane.height() - 1) / y))

    print(f"The total multiplied number is {result}")


def count_trees():
    my_plane = Plane2D("input_data.txt")
    part_one(my_plane)
    part_two(my_plane)


if __name__ == '__main__':
    count_trees()
