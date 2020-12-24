from typing import List, Set, Tuple
import re


def split_join(lst: List[str], q: str):
    r = []
    for p in lst:
        r += filter(len, re.split(f'({q})', p))
    return r


class ConwayHexTiles:
    black: Set[Tuple[int, int]]

    def __init__(self):
        self.black = set()

    @staticmethod
    def __parse_tile(line: str) -> Tuple[int, int]:
        dirs = {
            'e':  (2, 0),
            'w':  (-2, 0),
            'se': (1, -1),
            'sw': (-1, -1),
            'ne': (1, 1),
            'nw': (-1, 1),
        }

        temp = [line]
        for direction in ['se', 'sw', 'nw', 'ne']:
            temp = split_join(temp, direction)

        chunks = []
        for chunk in temp:
            if chunk in dirs.keys():
                chunks.append(chunk)
            else:
                for c in list(chunk):
                    chunks.append(c)

        result = (0, 0)
        for chunk in chunks:
            d = dirs[chunk]
            result = (result[0] + d[0], result[1] + d[1])

        return result

    def add_tile(self, line: str) -> None:
        tile_pos = self.__parse_tile(line)
        if tile_pos in self.black:
            self.black.remove(tile_pos)
        else:
            self.black.add(tile_pos)

    def neighbours(self, pos: Tuple[int, int]) -> int:
        result = 0

        for direction in [(2, 0), (-2, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]:
            if (pos[0] + direction[0], pos[1] + direction[1]) in self.black:
                result += 1

        return result

    def gen_step(self) -> None:
        directions = [(0, 0), (2, 0), (-2, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
        new_black = set()
        checked = set()
        for b in self.black:
            for direction in directions:
                tile_pos = (b[0] + direction[0], b[1] + direction[1])
                if tile_pos in checked:
                    continue
                checked.add(tile_pos)
                n = self.neighbours(tile_pos)
                if (tile_pos in self.black and n in {1, 2}) or (tile_pos not in self.black and n == 2):
                    new_black.add(tile_pos)
        self.black = new_black


def part_one(tiles: ConwayHexTiles) -> None:
    result = len(tiles.black)
    print(f"Result for part one is {result}")


def part_two(tiles: ConwayHexTiles) -> None:
    for _ in range(100):
        tiles.gen_step()
    result = len(tiles.black)
    print(f"Result for part two is {result}")


def main() -> None:
    source = "input_data.txt"
    tiles = ConwayHexTiles()
    with open(source) as fh:
        for line in fh:
            tiles.add_tile(line.rstrip())

    part_one(tiles)
    part_two(tiles)


if __name__ == '__main__':
    main()
