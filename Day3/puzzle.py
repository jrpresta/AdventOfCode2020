from functools import reduce

class SkiSlope:
    def __init__(self, slope_text):
        self.slope_text = slope_text
        self.width = len(slope_text[0])
        self.height = len(slope_text)
        self.trees = self.identify_tree_coordinates()

    def identify_tree_coordinates(self):
        coordinates = []

        for i, row in enumerate(self.slope_text):
            for j, v in enumerate(row):
                if v == '#':
                    coordinates.append((j, i))

        return coordinates


class Skier:
    def __init__(self, x, y, x_delta, y_delta, ski_slope):
        self.x = x
        self.y = y
        self.x_delta = x_delta
        self.y_delta = y_delta
        self.ski_slope = ski_slope
        self.trees_hit = 0

    def ski(self):
        while self.y <= self.ski_slope.height:
            self.advance()

            if (self.x, self.y) in self.ski_slope.trees:
                self.trees_hit += 1

    def advance(self):
        self.x += self.x_delta
        # incorporating horizontal wrap-around
        self.x = self.x % self.ski_slope.width
        self.y += self.y_delta


def main1(input):
    # CONSTANTS
    down_step = 1
    right_step = 3

    with open(input, 'r') as f:
        ss = SkiSlope([v.strip() for v in f.readlines()])

    skier = Skier(0, 0, right_step, down_step, ss)
    skier.ski()

    return skier.trees_hit


def create_and_run_skier(right, down, ss):
    skier = Skier(0, 0, right, down, ss)
    skier.ski()
    return skier.trees_hit

def main2(input):
    slope_candidates = [(1,1), (3,1), (5,1), (7,1), (1,2)]
    with open(input, 'r') as f:
        ss = SkiSlope([v.strip() for v in f.readlines()])

    return reduce(lambda x, y: x * y, [create_and_run_skier(sc[0], sc[1], ss) for sc in slope_candidates])


if __name__ == '__main__':
    input_file = './input.txt'

    print(main1(input_file))
    print(main2(input_file))
