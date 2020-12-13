from typing import Tuple


class ShipNavigation:
    x: int
    y: int
    direction: Tuple[int, int]

    def __init__(self, init_x: int = -1, init_y: int = 0):
        self.x = 0
        self.y = 0
        self.direction = (init_x, init_y)

    def _rotate_left(self, times: int) -> None:
        rotation = {
            (-1, 0): (0, 1),   # EAST  -> NORTH
            (0, 1): (1, 0),    # NORTH -> WEST
            (1, 0): (0, -1),   # WEST  -> SOUTH
            (0, -1): (-1, 0)   # SOUTH -> EAST
        }

        for _ in range(times):
            self.direction = rotation[self.direction]

    def _rotate_right(self, times: int) -> None:
        rotation = {
            (-1, 0): (0, -1),  # EAST  -> SOUTH
            (0, -1): (1, 0),   # SOUTH -> WEST
            (1, 0): (0, 1),    # WEST  -> NORTH
            (0, 1): (-1, 0)    # NORTH -> EAST
        }

        for _ in range(times):
            self.direction = rotation[self.direction]

    def _change_direction(self, instruction: str) -> None:
        value = int(instruction[1:]) // 90
        if instruction[0] == 'R':
            self._rotate_right(value)
        else:
            self._rotate_left(value)

    def _move(self, instruction: str) -> None:
        parse_direction = {
            'N': (1, 0),
            'E': (-1, 0),
            'S': (0, -1),
            'W': (1, 0),
            'F': self.direction
        }
        value = int(instruction[1:])
        direction = parse_direction[instruction[0]]

        self.x += direction[0] * value
        self.y += direction[1] * value

    def navigate(self, input_path: str) -> None:
        with open(input_path) as fh:
            for line in fh:
                line = line.strip()
                if line[0] == 'R' or line[0] == 'L':
                    self._change_direction(line)
                else:
                    self._move(line)

    def _rotate_right_relative(self, value: int) -> None:
        x = self.direction[0]
        y = self.direction[1]

        for _ in range(value):
            x, y = -y, x

        self.direction = (x, y)

    def _rotate_left_relative(self, value: int) -> None:
        x = self.direction[0]
        y = self.direction[1]

        for _ in range(value):
            x, y = y, -x

        self.direction = (x, y)

    def _change_direction_relative(self, instruction: str) -> None:
        value = int(instruction[1:]) // 90
        if instruction[0] == 'R':
            self._rotate_right_relative(value)
        else:
            self._rotate_left_relative(value)

    def _move_relative(self, instruction: str) -> None:
        value = int(instruction[1:])
        parse_waypoint = {
            'N': (0, 1),
            'E': (-1, 0),
            'S': (0, -1),
            'W': (1, 0),
        }
        if instruction[0] == 'F':
            self.x += self.direction[0] * value
            self.y += self.direction[1] * value
        else:
            x = self.direction[0] + parse_waypoint[instruction[0]][0] * value
            y = self.direction[1] + parse_waypoint[instruction[0]][1] * value
            self.direction = (x, y)

    def navigate_relative(self, input_path: str) -> None:
        with open(input_path) as fh:
            for line in fh:
                line = line.strip()
                if line[0] == 'R' or line[0] == 'L':
                    self._change_direction_relative(line)
                else:
                    self._move_relative(line)

    def manhattan(self) -> int:
        return abs(self.x) + abs(self.y)


def part_one() -> None:
    navigation = ShipNavigation()
    navigation.navigate("input_data.txt")
    print(f"Result for part one is {navigation.manhattan()}")


def part_two() -> None:
    navigation = ShipNavigation(-10, 1)
    navigation.navigate_relative("input_data.txt")
    print(f"Result for part two is {navigation.manhattan()}")


def main() -> None:
    part_one()
    part_two()


if __name__ == '__main__':
    main()
