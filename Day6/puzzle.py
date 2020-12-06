
class Plane:
    def __init__(self, data):
        self.groups = [Group(v) for v in data.split('\n\n')]

    def count_answer_size(self, set_fn):
        return sum([v.get_group_answers(set_fn) for v in self.groups])


class Group:
    def __init__(self, group):
        self.members = [v for v in group.split('\n') if v != '']

    def get_group_answers(self, set_fn):
        return len(set_fn(*[set(v) for v in self.members]))


def main1(input_file):
    with open(input_file, 'r') as f:
        plane = Plane(f.read())

    return plane.count_answer_size(set.union)


def main2(input_file):
    with open(input_file, 'r') as f:
        plane = Plane(f.read())

    return plane.count_answer_size(set.intersection)


if __name__ == '__main__':
    input_file = './input.txt'

    print(main1(input_file))
    print(main2(input_file))
