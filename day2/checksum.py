""" checksum.py
Solver for day 2 of adventofcode.com.
"""


def calculate_row_even_div(row):
    """ calculate_row_even_div(row) -> int()
    Finds two numbers in row that are evenly divesable and returns the product
    of that division.
    """
    tmp_row = row[1:]
    for divisor in row:
        for dividend in tmp_row:
            if dividend % divisor == 0:
                return dividend / divisor
            elif divisor % dividend == 0:
                return divisor / dividend
        tmp_row = tmp_row[1:]


def calculate_division_checksum(spreadsheet):
    """ calculate_division_checksum(spreadsheet) -> int()
    Checks each row in spreadsheet for numbers that are evenly divisable.
    Returns the total sum of the products of each division.
    """
    tot = 0
    for row in spreadsheet:
        tot += calculate_row_even_div(row)
    return tot


def calculate_min_max_checksum(spreadsheet):
    """ calculate_checksum(spreadsheet) -> int()
    Given a 2 dimensional array, calculates the row sum for each row and adds
    the rows to a total checksum. The total checksum is then returned.
    """
    tot = 0
    for row in spreadsheet:
        tot += calculate_row_min_max(row)
    return tot


def calculate_row_min_max(row):
    """ calculate_row(row) -> int()
    Finds max and min values in row and subtracts min from max and returns the
    result.
    """
    return max(row) - min(row)


def main():
    """ main() -> void
    Reads input data from file and sends that to calculate_checksum by making
    it a python list first.
    Prints the total checksum.
    """
    with open('input_data.txt', 'r') as in_data:
        spreadsheet = []
        for row in in_data:
            num_row = [int(x) for x in row.split()]
            spreadsheet.append(num_row)

        print calculate_division_checksum(spreadsheet)


if __name__ == '__main__':
    main()
