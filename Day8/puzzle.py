import copy


class Instruction:
    def __init__(self, type, value):
        self.type = type
        self.value = value
        self.has_been_seen = False

    def __repr__(self):
        return f'{self.type}_{self.value}'

    def __str__(self):
        return self.__repr__()


class InstructionSet:
    def __init__(self, instructions):
        self.instructions = instructions
        self.cursor_position = 0
        self.accumulator = 0
        self.fns = {'nop': self.nop, 'jmp': self.jump, 'acc': self.accumulate}

    def execute(self):
        while (self.ready_to_terminate()) or (not self.current_instruction().has_been_seen):
            if self.ready_to_terminate():
                return Exit(1, self.accumulator)

            self.mark_current_instruction()
            self.fns[self.current_instruction().type](self.current_instruction().value)
        return Exit(0, self.accumulator)

    def nop(self, _):
        self.move_cursor(1)

    def jump(self, magnitude):
        self.move_cursor(magnitude)

    def accumulate(self, magnitude):
        self.accumulator += magnitude
        self.move_cursor(1)

    def move_cursor(self, magnitude):
        self.cursor_position += magnitude

    def current_instruction(self):
        return self.instructions[self.cursor_position]

    def mark_current_instruction(self):
        self.current_instruction().has_been_seen = True

    def ready_to_terminate(self):
        return self.cursor_position == len(self.instructions)


class Exit:
    def __init__(self, status, value):
        self.status = status
        self.value = value


def parse_instruction_ln(ln):
    splt = ln.split()
    return Instruction(splt[0], int(splt[1]))


def modifyIS(instructions, idx):
    switch_value = {'acc': 'acc', 'nop': 'jmp', 'jmp': 'nop'}
    instructions[idx].type = switch_value[instructions[idx].type]

    return instructions


def main1(input_file):
    with open(input_file, 'r') as f:
        instructions = [parse_instruction_ln(v) for v in f.readlines()]

    return InstructionSet(instructions).execute().value


def main2(input_file):
    with open(input_file, 'r') as f:
        instructions = [parse_instruction_ln(v) for v in f.readlines()]

    exits = [InstructionSet(modifyIS(copy.deepcopy(instructions), i)).execute() for i in range(len(instructions))]
    return [e.value for e in exits if e.status == 1][0]


if __name__ == '__main__':
    input_file = './input.txt'

    print(main1(input_file))
    print(main2(input_file))
