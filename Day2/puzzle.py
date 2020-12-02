
class PasswordRules:
    def __init__(self, min, max, letter, pw):
        self.min = int(min)
        self.max = int(max)
        self.letter = letter
        self.pw = pw

    def validate(self):
        count = self.pw.count(self.letter)
        return self.min <= count <= self.max


class PasswordRulesNew:
    def __init__(self, first_position, second_position, letter, pw):
        self.first_position = int(first_position)
        self.second_position = int(second_position)
        self.letter = letter
        self.pw = pw

    def validate(self):
        fp_valid = self.pw[self.first_position-1] == self.letter
        sp_valid = self.pw[self.second_position-1] == self.letter

        return fp_valid + sp_valid == 1


def parse_lines(ln):
    """Parse apart the format from the given txt file"""
    triplets = ln.split()

    min = triplets[0].split('-')[0]
    max = triplets[0].split('-')[1]
    letter = triplets[1].split(':')[0]
    pw = triplets[2]

    return (min, max, letter, pw)


def main1(input_path):
    with open(input_path, 'r') as f:
        data = [parse_lines(ln) for ln in f.readlines()]
        data = [PasswordRules(v[0], v[1], v[2], v[3]) for v in data]

    return sum([p.validate() for p in data])


def main2(input_path):
    with open(input_path, 'r') as f:
        data = [parse_lines(ln) for ln in f.readlines()]
        data = [PasswordRulesNew(v[0], v[1], v[2], v[3]) for v in data]

    return sum([p.validate() for p in data])


if __name__ == '__main__':
    input_file = './input.txt'
    
    print(main1(input_file))
    print(main2(input_file))
