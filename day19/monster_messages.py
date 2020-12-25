from typing import List, Tuple
import re


class RegularMessages:
    rules: dict
    final: set

    def __init__(self):
        self.rules = {}
        self.final = set()

    def get_regular(self, rule: int) -> str:
        if rule in self.final:
            return self.rules[rule]

        result = ''
        for rule_set in self.rules[rule]:
            if result != '':
                result += '|'

            for rule_part in rule_set:
                result += self.get_regular(rule_part)
        return f'(?:{result})'

    def get_regular2(self, rule: int) -> str:
        if rule in self.final:
            return self.rules[rule]

        result = ''
        for rule_set in self.rules[rule]:
            if result != '':
                result += '|'

            for rule_part in rule_set:
                if rule_part == 8:  # this part of solution was borrowed from reddit user u/ihopethisnamewillfi
                    result += f"(?:{self.get_regular2(42)})+"
                elif rule_part == 11:
                    result += f"(?:{'|'.join(map(lambda c: self.get_regular2(42) * c + self.get_regular2(31) * c, range(1, 11)))})"
                else:
                    result += self.get_regular(rule_part)
        return f'(?:{result})'

    def load_rule(self, rule: str) -> None:
        parts = rule.split(':')
        k = int(parts[0])
        v = parts[1].strip().split()
        if v[0][0] == '"':
            self.final.add(k)
            self.rules[k] = v[0][1:-1]
            return

        self.rules[k] = []
        temp = []

        for part in v:
            if part == '|':
                self.rules[k].append(temp)
                temp = []
                continue

            temp.append(int(part))

        self.rules[k].append(temp)


def part_one(reg_mes: RegularMessages, messages: List[str]) -> None:
    regular = '^' + reg_mes.get_regular(0) + '$'
    compiled_reg = re.compile(regular)
    result = sum(1 for msg in messages if compiled_reg.match(msg))

    print(f'Result for part one is {result}')


def part_two(reg_mes: RegularMessages, messages: List[str]) -> None:
    regular = f"^{reg_mes.get_regular2(0)}$"
    compiled_reg = re.compile(regular)
    result = sum(1 for msg in messages if compiled_reg.match(msg))

    print(f'Result for part two is {result}')


def load_data(input_path: str) -> Tuple[List[str], List[str]]:
    rule_lines = []
    messages = []
    target = rule_lines
    with open(input_path) as fh:
        for line in fh:
            line = line.strip()
            if line == '':
                target = messages
                continue

            target.append(line)

    return rule_lines, messages


def main() -> None:
    source = "input_data.txt"
    r, m = load_data(source)
    reg = RegularMessages()
    for rule in r:
        reg.load_rule(rule)

    part_one(reg, m)
    part_two(reg, m)


if __name__ == '__main__':
    main()
