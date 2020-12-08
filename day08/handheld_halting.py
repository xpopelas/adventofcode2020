from typing import List, Tuple


class Computer:
    head_pos: int
    amount: int
    instructions = List[Tuple[str, int]]

    def __init__(self):
        self.head_pos = 0
        self.amount = 0
        self.instructions = []

    def reset_values(self):
        self.head_pos = 0
        self.amount = 0

    def load_instructions(self, input_path: str = "input_data.txt") -> None:
        with open(input_path) as fh:
            for line in fh:
                line = line.strip()
                self.instructions.append(tuple([line[:3], int(line[4:])]))

    def reverse_instruction(self, index: int) -> bool:
        instruction = self.instructions[index]
        reverse_f = {"jmp": "nop", "nop": "jmp", "acc": "acc"}
        self.instructions[index] = tuple([reverse_f[instruction[0]], instruction[1]])
        return instruction in {"jmp", "nop"}

    def perform_instruction(self) -> None:
        instruction = self.instructions[self.head_pos]
        if instruction[0] == 'acc':
            self.amount += instruction[1]
            self.head_pos += 1
        elif instruction[0] == 'jmp':
            self.head_pos += instruction[1]
        else:
            self.head_pos += 1

    def run(self) -> bool:
        self.reset_values()
        seen_instructions = set()
        while self.head_pos not in seen_instructions:
            seen_instructions.add(self.head_pos)
            if self.head_pos == len(self.instructions):
                return True
            self.perform_instruction()
        return False


def part_one(computer: Computer) -> None:
    computer.reset_values()
    computer.run()
    print(f"Computer computed value of {computer.amount} on halt")


def part_two(computer: Computer) -> None:
    computer.reset_values()
    index = 0
    while index < len(computer.instructions):
        while computer.instructions[index][0] == "acc":
            index += 1
        computer.reverse_instruction(index)

        computer.reset_values()
        if computer.run():
            computer.reverse_instruction(index)
            print(f"Invalid instruction was at index {index}")
            print(f"Invalid instruction was '{computer.instructions[index][0]} {computer.instructions[index][1]}'")
            print(f"Accumulated value is {computer.amount}")
            return

        computer.reverse_instruction(index)
        index += 1
    print(f"Welp, something went wrong")


def main():
    computer = Computer()
    computer.load_instructions()
    part_one(computer)
    part_two(computer)


if __name__ == '__main__':
    main()
