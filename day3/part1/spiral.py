""" spiral.py
Attempt to solve day 3 of advent of code.
"""


def generate(stop):
    """ generate(stop) -> [tuple()]
    Generate spiral matrix indexes until stop

    stop = int()
    """
    matrix = [(0, 0)]
    directions = ['right', 'up', 'left', 'down']
    row_steps = 0
    row_max = 1

    for index in range(len(matrix), stop+1):
        direction = directions.pop(0)

        while row_steps < row_max and len(matrix) < stop:
            (last_x, last_y) = matrix[-1]

            if direction == 'right':
                matrix.append((last_x+1, last_y))
            elif direction == 'up':
                matrix.append((last_x, last_y+1))
            elif direction == 'left':
                matrix.append((last_x-1, last_y))
            else:
                matrix.append((last_x, last_y-1))

            row_steps += 1

        directions.append(direction)
        row_steps = 0

        if index % 2 == 0:
            row_max += 1

    return matrix


def steps_to(index):
    """ steps_to(index) -> int()
    Calculate the carrying distance from index to 0.
    Index is given as which square to calculate from.

    index = int()
    """
    matrix = generate(index)
    (x_coor, y_coor) = matrix[-1]
    print matrix[-1]

    return abs(x_coor) + abs(y_coor)


def main():
    """ main()
    Solve puzzle
    """
    print steps_to(325489)


if __name__ == '__main__':
    main()
