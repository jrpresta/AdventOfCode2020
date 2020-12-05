
def seat_id(input):
    row_instructions = input[:7]
    col_instructions = input[7:10]

    row = list(range(128))
    col = list(range(8))

    for ri in row_instructions:
        row = halve_area(ri, row)

    for ci in col_instructions:
        col = halve_area(ci, col)

    return row[0]*8 + col[0]


def halve_area(instruction, candidate_list):
    midpoint = int(len(candidate_list) / 2)

    if instruction in ['F', 'L']:
        return candidate_list[:midpoint]
    if instruction in ['B', 'R']:
        return candidate_list[midpoint:]


def neighbor_seats_exist(center_id, ids):
    return (center_id+1 in ids) & (center_id-1 in ids)


def main1(input_file):
    with open(input_file, 'r') as f:
        input = f.readlines()

    return max([seat_id(v) for v in input])


def main2(input_file):
    with open(input_file, 'r') as f:
        input = f.readlines()

    ids = [seat_id(v) for v in input]
    missing_ids = set(range(max(ids))).difference(set(ids))
    return [mi for mi in missing_ids if neighbor_seats_exist(mi, ids)]


if __name__ == '__main__':
    input_file = './input.txt'

    print(main1(input_file))
    print(main2(input_file))
