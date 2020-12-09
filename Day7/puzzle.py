import re

class Bag:
    def __init__(self, bag):
        self.bag = bag


def parse_bag_rules(bag_rule_ln):
    parent_bag, children_bags = bag_rule_ln.split(" bags contain ")
    children_bags = children_bags.replace('.', '').split(', ')

    if children_bags == ['no other bags']:
        return (Bag(parent_bag), [])
    else:
        children_bags = [Bag(remove_digits(v)) for v in children_bags]
        return (Bag(parent_bag), children_bags)


def parse_bag_rules_with_multiple(bag_rule_ln):
    parent_bag, children_bags = bag_rule_ln.split(" bags contain ")
    children_bags = children_bags.replace('.', '').split(', ')

    if children_bags == ['no other bags']:
        return (Bag(parent_bag), [])
    else:
        cbs = []

        for cb in children_bags:
            count = int(re.findall(r'\d+', cb)[0])
            cbs += count*[Bag(remove_digits(cb))]
        return (Bag(parent_bag), cbs)


def remove_bag_string(x):
    return x.replace(' bags', '').replace(' bag', '')


def remove_digits(x):
    return ''.join([i for i in x if not i.isdigit()]).strip()


def flatten_list(lst):
    return [inner for outer in lst for inner in outer]


def make_descender(bag_map, target_bag):
    def descend(bag, seen):
        new_seen = seen + [bag]
        children_bags = bag_map[bag]

        if not children_bags:
            return [None]
        if target_bag in children_bags:
            return new_seen

        return flatten_list([descend(cb, new_seen) for cb in children_bags])
    return descend


def sum_child_bags(bag, bag_map):
    children_bags = bag_map[bag]
    return 1 + sum([sum_child_bags(cb, bag_map) for cb in children_bags])


def main1(input_file):
    with open(input_file, 'r') as f:
        bag_pairs = [parse_bag_rules(v.strip()) for v in f.readlines()]

    bag_map = {v[0].bag: [remove_bag_string(cb.bag) for cb in v[1]] for v in bag_pairs}
    descender = make_descender(bag_map, 'shiny gold')

    out_bag_set = set(flatten_list([descender(b, []) for b in bag_map]))
    out_bag_set.discard(None)
    return len(out_bag_set)


def main2(input_file):
    with open(input_file, 'r') as f:
        bag_pairs = [parse_bag_rules_with_multiple(v.strip()) for v in f.readlines()]

    bag_map = {v[0].bag: [remove_bag_string(cb.bag) for cb in v[1]] for v in bag_pairs}
    return sum_child_bags('shiny gold', bag_map) - 1


if __name__ == '__main__':
    input_file = './input.txt'

    print(main1(input_file))
    print(main2(input_file))
