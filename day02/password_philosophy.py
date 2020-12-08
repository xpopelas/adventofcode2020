from typing import List, Dict


def input_to_obj(input_path: str) -> List[Dict]:
    result = []
    with open(input_path, 'r') as fh:
        for line_txt in fh:
            chunks = line_txt.split()
            password = {
                "min": int(chunks[0].split('-')[0]),
                "max": int(chunks[0].split('-')[1]),
                "req_char": chunks[1][0],
                "password": chunks[2]
            }
            result.append(password)
    return result


def verify_pass(password: Dict) -> bool:
    return password["min"] <= len([1 for i in password["password"] if i == password["req_char"]]) <= password["max"]


def part_one(data_dict: List[Dict]) -> None:
    print(f"There are {len([1 for i in data_dict if verify_pass(i)])} valid passwords out of "
          f"{len(data_dict)} for part1")


def verify_pass2(password: Dict) -> bool:
    res = 0
    for phr in ["min", "max"]:
        if password["password"][password[phr] - 1] == password["req_char"]:
            res += 1
    return res == 1


def part_two(data_dict: List[Dict]) -> None:
    print(f"There are {len([1 for i in data_dict if verify_pass2(i)])} valid passwords out of "
          f"{len(data_dict)} for part2")


def main():
    data_dict = input_to_obj("input_data.txt")
    part_one(data_dict)
    part_two(data_dict)


if __name__ == '__main__':
    main()
