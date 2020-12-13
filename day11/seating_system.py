from typing import List, Callable


class GameOfSeat:
    seats: List[List[str]]

    def __init__(self, input_file):
        self.seats = self._load_seats(input_file)

    @staticmethod
    def _load_seats(input_file) -> List[List[str]]:
        with open(input_file) as fh:
            return [list(line.strip()) for line in fh]

    def rows(self) -> int:
        return len(self.seats)

    def cols(self) -> int:
        return len(self.seats[0])

    def is_empty_seat(self, x: int, y: int) -> bool:
        return self.seats[y][x] == 'L'

    def is_taken_seat(self, x: int, y: int) -> bool:
        return self.seats[y][x] == '#'

    def is_floor(self, x: int, y: int) -> bool:
        return self.seats[y][x] == '.'

    def total_occupied(self) -> int:
        result = 0
        for row in self.seats:
            for seat in row:
                if seat == '#':
                    result += 1
        return result

    def neighbours(self, x: int, y: int) -> int:
        result = 0
        for i in range(max([x - 1, 0]), min([x + 2, self.cols()])):
            for j in range(max([y - 1, 0]), min([y + 2, self.rows()])):
                if i == x and j == y:
                    continue
                if self.is_taken_seat(i, j):
                    result += 1
        return result

    def neighbours_seen_occupied(self, x: int, y: int) -> int:
        result = 0
        for ax in [-1, 0, 1]:
            for ay in [-1, 0, 1]:
                if ax == 0 and ay == 0:
                    continue

                nx = ax + x
                ny = ay + y

                while nx in range(self.cols()) and ny in range(self.rows()):
                    if self.is_empty_seat(nx, ny):
                        break

                    if self.is_taken_seat(nx, ny):
                        result += 1
                        break

                    nx += ax
                    ny += ay

        return result

    def gen_step(self) -> bool:
        new_seats = []

        for y in range(self.rows()):
            to_add = []
            for x in range(self.cols()):
                if self.is_floor(x, y):
                    to_add.append('.')
                elif self.is_empty_seat(x, y):
                    if self.neighbours(x, y) == 0:
                        to_add.append('#')
                    else:
                        to_add.append('L')
                elif self.is_taken_seat(x, y):
                    if self.neighbours(x, y) >= 4:
                        to_add.append('L')
                    else:
                        to_add.append('#')
            new_seats.append(to_add)

        result = new_seats != self.seats
        self.seats = new_seats

        return result

    def gen2_step(self) -> bool:
        new_seats = []

        for y in range(self.rows()):
            to_add = []
            for x in range(self.cols()):
                if self.is_floor(x, y):
                    to_add.append('.')
                    continue

                neighbours = self.neighbours_seen_occupied(x, y)
                if self.is_empty_seat(x, y):
                    if neighbours == 0:
                        to_add.append('#')
                    else:
                        to_add.append('L')
                elif self.is_taken_seat(x, y):
                    if neighbours >= 5:
                        to_add.append('L')
                    else:
                        to_add.append('#')
            new_seats.append(to_add)

        result = new_seats != self.seats
        self.seats = new_seats

        return result


def part_one(game: GameOfSeat) -> None:
    steps = 0
    while game.gen_step():
        steps += 1
    print(f"Result for part one is {game.total_occupied()}")


def part_two(game: GameOfSeat) -> None:
    steps = 0
    while game.gen2_step():
        steps += 1
    print(f"Result for part two is {game.total_occupied()}")


def main() -> None:
    print("This solutions isn't as fast, so this might take a while...")
    part_one(GameOfSeat("input_data.txt"))
    part_two(GameOfSeat("input_data.txt"))


if __name__ == '__main__':
    main()
