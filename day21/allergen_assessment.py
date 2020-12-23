from typing import Dict, List, Tuple


class IngResolver:
    labels: List[Tuple[List[str], List[str]]]
    allergens: Dict
    occurrences: Dict

    def __init__(self):
        self.labels = []
        self.allergens = {}
        self.occurrences = {}

    def load_input(self, input_path: str):
        with open(input_path) as fh:
            for line in fh:
                line = line.rstrip().replace(')', '').split(' (contains ')
                self.labels.append((line[0].split(' '), line[1].split(', ')))

    def resolve(self):
        for label in self.labels:
            for allergen in label[1]:
                if allergen in self.allergens:
                    self.allergens[allergen] = [lab for lab in label[0] if lab in self.allergens[allergen]]
                else:
                    self.allergens[allergen] = label[0]
            for ingredient in label[0]:
                self.occurrences[ingredient] = self.occurrences.get(ingredient, 0) + 1


def part_one(ir: IngResolver) -> None:
    result = 0
    for ingredient, amount in ir.occurrences.items():
        if all(ingredient not in v for v in ir.allergens.values()):
            result += amount

    print(f'Result for part one is {result}')


def part_two(ir: IngResolver) -> None:
    used = set()
    while any(len(a) > 1 for a in ir.allergens.values()):
        for allergen, ingredient in ir.allergens.items():
            if len(ingredient) == 1 and ingredient[0] not in used:
                used.add(ingredient[0])
            elif len(ingredient) > 1:
                for i in used:
                    if i in ingredient:
                        ir.allergens[allergen].remove(i)

    result = ','.join(v[0] for k, v in sorted(ir.allergens.items(), key=lambda k: k[0]))
    print(f'Result for part two is {result}')


def main():
    source = "input_data.txt"
    ir = IngResolver()
    ir.load_input(source)
    ir.resolve()
    part_one(ir)
    part_two(ir)


if __name__ == '__main__':
    main()
