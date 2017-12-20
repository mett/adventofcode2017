""" punchcard.py
Implementation to solve day5 of advent of code.
"""


def run(instructions):
    """ run(instructions)
    Runs a series of instructions according to the ruleset given in day5.
    """
    steps = 0
    index = 0

    while True:
        try:
            next_index = instructions[index]
        except IndexError:
            return steps

        instructions[index] = next_index + 1
        steps += 1
        index += next_index


def main():
    """ main()
    Read file input and put this through the run algorithm.
    """
    with open('input.txt', 'r') as file_data:
        instructions = []
        for point in file_data:
            instructions.append(int(point))
        print run(instructions)


if __name__ == '__main__':
    main()
