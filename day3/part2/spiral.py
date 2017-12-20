""" spiral.py
Attempt to solve day 3 of advent of code.
"""


def get_preceeding_square(stop):
    """ get_preceeding_square(stop) -> int()
    Returns the value of the square before we go over the given stop.

    stop = int()
    """
    matrix = {
        (0, 0): 1,
        (1, 0): 1
    }
    directions = ['u', 'l', 'd', 'r']

    row_steps = 0
    row_max = 1
    index = 1
    last_square = 1
    x_co = 1
    y_co = 0

    while last_square <= stop:
        index += 1
        direction = directions.pop(0)

        while row_steps < row_max:
            if direction == 'r':
                x_co += 1
            elif direction == 'u':
                y_co += 1
            elif direction == 'l':
                x_co -= 1
            else:
                y_co -= 1

            square_value = calculate_square_value(x_co, y_co, matrix)
            matrix[(x_co, y_co)] = square_value

            if square_value >= stop:
                print matrix
                print square_value
                print last_square
                return last_square

            last_square = square_value
            row_steps += 1

        directions.append(direction)
        row_steps = 0

        if index % 2 == 0:
            row_max += 1

    return last_square


def calculate_square_value(x_co, y_co, matrix):
    """ calculate_square_value(x_co, y_co, matrix) -> int()
    By looking at the neighbouring squares, returns the total value for those
    squares.
    """
    value = 0

    if (x_co+1, y_co) in matrix:  # check square to the right
        value += matrix[(x_co+1, y_co)]

    if (x_co-1, y_co) in matrix:  # check square to the left
        value += matrix[(x_co-1, y_co)]

    if (x_co, y_co+1) in matrix:  # check square above
        value += matrix[(x_co, y_co+1)]

    if (x_co, y_co-1) in matrix:  # check square below
        value += matrix[(x_co, y_co-1)]

    if (x_co+1, y_co-1) in matrix:  # check square diagonally right below
        value += matrix[(x_co+1, y_co-1)]

    if (x_co+1, y_co+1) in matrix:  # check square diagonally right above
        value += matrix[(x_co+1, y_co+1)]

    if (x_co-1, y_co+1) in matrix:  # check square diagonally left above
        value += matrix[(x_co-1, y_co+1)]

    if (x_co-1, y_co-1) in matrix:  # check square diagonally left below
        value += matrix[(x_co-1, y_co-1)]

    return value


def main():
    """ main()
    Solve puzzle
    """
    print get_preceeding_square(325489)


if __name__ == '__main__':
    main()
