def puzzle_1(file_path):
    with open(file_path, 'r') as f:
        values = [int(v.strip()) for v in f.readlines()]

    for i in values:
        for j in values:
            if i + j == 2020: return i*j

def puzzle_2(file_path):
    with open(file_path, 'r') as f:
        values = [int(v.strip()) for v in f.readlines()]

    for i in values:
        for j in values:
            for k in values:
                if i + j + k == 2020: return i*j*k


if __name__ == '__main__':
    input_file = './input.csv'

    print(puzzle_1(input_file))
    print(puzzle_2(input_file))
