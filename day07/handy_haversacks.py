from __future__ import annotations
from typing import List, Tuple


class BagNode:
    color: str
    contains: List[Tuple[int, BagNode]]
    contained_by: List[Tuple[int, BagNode]]

    def __init__(self, color: str):
        self.color = color
        self.contains = []
        self.contained_by = []
        self.discovered = False

    def add_contain(self, count: int, node: BagNode) -> None:
        self.contains.append((count, node))
        node.contained_by.append((count, self))

    def count_color_ownership(self) -> int:
        if self.discovered:
            return 0
        self.discovered = True
        return 1 + sum([bag[1].count_color_ownership() for bag in self.contained_by])

    def count_owned_bags(self) -> int:
        return 1 + sum([bag[0] * bag[1].count_owned_bags() for bag in self.contains])


def create_all_nodes(input_path: str = "input_data.txt") -> List[BagNode]:
    result = []
    with open(input_path) as fh:
        for line in fh:
            line = line.strip()
            result.append(BagNode(line.split(" contain ")[0][:-5]))
    return result


def connect_all_nodes(nodes: List[BagNode], input_path: str = "input_data.txt") -> None:
    with open(input_path) as fh:
        for line in fh:
            source, targets = line.strip().strip(".").split(" contain ")
            if targets == "no other bags":
                continue
            source = [bag for bag in nodes if bag.color == source[:-5]][0]
            for target in targets.split(", "):
                count = int(target[0])
                target = target[2:-4].strip()
                source.add_contain(count, [bag for bag in nodes if bag.color == target][0])


def set_all_undiscovered(nodes: List[BagNode]) -> None:
    for node in nodes:
        node.discovered = False


def part_one(nodes: List[BagNode]) -> None:
    set_all_undiscovered(nodes)
    shiny_gold = [bag for bag in nodes if bag.color == "shiny gold"][0]
    print(f"There are total of {shiny_gold.count_color_ownership() - 1} colors owning your bag")


def part_two(nodes: List[BagNode]) -> None:
    set_all_undiscovered(nodes)
    shiny_gold = [bag for bag in nodes if bag.color == "shiny gold"][0]
    print(f"There are total of {shiny_gold.count_owned_bags() - 1} owned bags")


def main():
    nodes = create_all_nodes()
    connect_all_nodes(nodes)
    part_one(nodes)
    part_two(nodes)


if __name__ == '__main__':
    main()
