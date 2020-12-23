from typing import Tuple
from collections import deque


def load_input(input_path: str) -> Tuple[deque, deque]:
    p1 = deque()
    p2 = deque()

    with open(input_path) as fh:
        for player in [p1, p2]:
            fh.readline()
            line = fh.readline().rstrip()
            while line:
                player.append(int(line))
                line = fh.readline().rstrip()

    return p1, p2


def calculate_score(q: deque) -> int:
    result = 0

    for index, val in enumerate(q):
        result += (len(q) - index) * val

    return result


def play_crab_combat(q1: deque, q2: deque) -> deque:
    while q1 and q2:
        a = q1.popleft()
        b = q2.popleft()

        if a < b:
            q2.append(b)
            q2.append(a)
        else:
            q1.append(a)
            q1.append(b)

    return q1 if q1 else q2


def play_recursive_combat(q1: deque, q2: deque) -> bool:
    history = set()
    while q1 and q2:
        current = tuple(q1), tuple(q2)
        if current in history:
            return False

        history.add(current)

        a = q1.popleft()
        b = q2.popleft()

        if a <= len(q1) and b <= len(q2):
            winner = play_recursive_combat(deque(list(q1)[:a]), deque(list(q2)[:b]))
        else:
            winner = a < b

        if winner:
            q2.append(b)
            q2.append(a)
        else:
            q1.append(a)
            q1.append(b)

    return not q1


def part_one(input_path: str) -> None:
    p1, p2 = load_input(input_path)
    winner = play_crab_combat(p1, p2)
    result = calculate_score(winner)

    print(f'Result for part one is {result}')


def part_two(input_path: str) -> None:
    p1, p2 = load_input(input_path)
    play_recursive_combat(p1, p2)
    result = calculate_score(p1 if p1 else p2)

    print(f'Result for part two is {result}')


def main():
    source = "input_data.txt"
    part_one(source)
    part_two(source)


if __name__ == '__main__':
    main()
