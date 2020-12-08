def part_one() -> None:
    total = 0
    with open("input_data.txt") as fh:
        letters = set()
        for line in fh:
            line = line.strip()
            if line == '':
                total += len(letters)
                letters = set()
                continue
            for letter in line:
                letters.add(letter)
        total += len(letters)
    print(f"There are total of {total} answers")


def part_two() -> None:
    total = 0
    with open("input_data.txt") as fh:
        group_answers = []
        for line in fh:
            line = line.strip()
            if line == '':
                total += len(set.intersection(*group_answers))
                group_answers = []
                continue
            temporary_set = set()
            for letter in line:
                temporary_set.add(letter)
            group_answers.append(temporary_set)
        total += len(set.intersection(*group_answers))
    print(f"There are total of {total} group answers")


def main():
    part_one()
    part_two()


if __name__ == '__main__':
    main()
