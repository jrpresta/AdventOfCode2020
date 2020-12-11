
def is_sum(value, preamble):
    for i, p in enumerate(preamble):
        diff = value - p
        if diff in set(preamble[:i] + preamble[:i+1]):
            return True
    else:
        return False


def sum_until_target(target, idx, data):
    accum = 0
    upper_bound = idx

    while accum < target:
        accum += data[upper_bound]
        upper_bound += 1

    if accum == target:
        data_range = data[idx:upper_bound+1]
        return (True, min(data_range) + max(data_range))
    return [False]

def main1(input_file):
    with open(input_file, 'r') as f:
        data = [int(v) for v in f.readlines()]

    PREAMBLE_LEN = 25

    for i in range(PREAMBLE_LEN, len(data)):
        pr = data[i-PREAMBLE_LEN: i]
        if not is_sum(data[i], pr):
            return data[i]


def main2(input_file):
    with open(input_file, 'r') as f:
        data = [int(v) for v in f.readlines()]
    target_value = main1(input_file)

    for i in range(len(data)):
        accum_result = sum_until_target(target_value, i, data)
        if accum_result[0]:
            return accum_result[1]

if __name__ == '__main__':
    input_file = './input.txt'

    print(main1(input_file))
    print(main2(input_file))
