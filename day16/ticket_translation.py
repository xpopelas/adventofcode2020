from typing import Tuple, List


def _load_dict(fh) -> dict:
    result = {}
    line = fh.readline().rstrip()
    while line != "":
        key, values = line.split(": ")
        values = values.split(" or ")
        value = set()
        for r in values:
            r = r.split("-")
            value = value.union(set(range(int(r[0]), int(r[1]) + 1)))
        result[key] = value
        line = fh.readline().rstrip()
    return result


def _load_data(input_path: str) -> Tuple[dict, List[int], List[List[int]]]:
    with open(input_path) as fh:
        fields = _load_dict(fh)
        fh.readline()
        your_ticket = [int(val) for val in fh.readline().rstrip().split(',')]
        fh.readline()
        fh.readline()
        nearby_tickets = []
        for line in fh:
            nearby_tickets.append([int(val) for val in line.rstrip().split(',')])

    return fields, your_ticket, nearby_tickets


def not_in_fields(fields: dict, value: int) -> bool:
    return not any(value in f for f in fields.values())


def part_one(fields: dict, nearby_tickets: List[List[int]]) -> List[List[int]]:
    result = 0

    valid_tickets = []
    for ticket in nearby_tickets:
        if any(not_in_fields(fields, v) for v in ticket):
            result += sum(v for v in ticket if not_in_fields(fields, v))
        else:
            valid_tickets.append(ticket)

    print(f"Result for part one is {result}")

    return valid_tickets


def part_two(fields: dict, your_ticket: List[int], nearby_tickets: List[List[int]]) -> None:
    result = 1
    total_set = set(range(len(fields.keys())))

    for _ in fields.copy():
        for k in fields.keys():
            v = fields[k]
            definitive = [p for p in total_set if all(tick[p] in v for tick in nearby_tickets)]
            if len(definitive) == 1:
                total_set.remove(definitive[0])
                del fields[k]

                if k.startswith("departure"):
                    result *= your_ticket[definitive[0]]

                break

    print(f"Result for part two is {result}")


def main() -> None:
    fields, your_ticket, nearby_tickets = _load_data("input_data.txt")
    nearby_tickets = part_one(fields, nearby_tickets)
    part_two(fields, your_ticket, nearby_tickets)


if __name__ == '__main__':
    main()
