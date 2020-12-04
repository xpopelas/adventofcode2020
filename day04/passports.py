import re
from typing import List


class Passport:
    def __init__(self, tokens):
        self.data_keys = {}
        self.load_tokens(tokens)

    def load_tokens(self, tokens: List[str]):
        for token in tokens:
            parts = token.split(':')
            self.data_keys[parts[0]] = parts[1]

    def has_req_keys(self):
        valid_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
        for key in valid_keys:
            if key not in self.data_keys:
                return False
        return True

    def is_valid_values(self, valid_values):
        if not self.has_req_keys():
            return False

        for key in valid_values:
            if self.data_keys[key] not in valid_values[key]:
                return False

        return True

    def is_valid_regex(self, key, regex):
        return regex.match(self.data_keys[key])


def line_to_tokens(line: str) -> List[str]:
    return [s.strip() for s in line.split()]


def file_to_tokens(input_path: str) -> List[List[str]]:
    result = []
    token = []
    with open(input_path, 'r') as fh:
        for line in fh:
            if line == '\n':
                if token:
                    result.append(token)
                token = []

            token += line_to_tokens(line)

    if token:
        result.append(token)

    return result


def get_valid_passports():
    tokens = file_to_tokens("input_data.txt")
    passports = []
    for token_bundle in tokens:
        passports.append(Passport(token_bundle))

    has_keys = [p for p in passports if p.has_req_keys()]
    print(f"There are total of {len(has_keys)} passports with required keys out of {len(passports)}")

    valid_values = {
        "byr": [str(byr) for byr in range(1920, 2003)],
        "iyr": [str(iyr) for iyr in range(2010, 2021)],
        "eyr": [str(eyr) for eyr in range(2020, 2031)],
        "hgt": [str(hgt) + 'cm' for hgt in range(150, 194)] + [str(hgt) + 'in' for hgt in range(59, 77)],
        "ecl": ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
    }

    valid_hcl = re.compile('^#[\d|a-f]{6}$')
    valid_pid = re.compile('^\d{9}$')

    has_valid_values = list(filter(lambda x: x.is_valid_values(valid_values), has_keys))
    has_valid_hcl = list(filter(lambda x: x.is_valid_regex('hcl', valid_hcl), has_valid_values))
    has_valid_pid = list(filter(lambda x: x.is_valid_regex('pid', valid_pid), has_valid_hcl))

    print(f"There are total of {len(has_valid_pid)} valid passports out of {len(passports)}")


if __name__ == '__main__':
    get_valid_passports()