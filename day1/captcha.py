""" captcha.py
Decode captcha input for Advent of Code day 1.
"""


def decode(data, part=1):
    """ decode(data) -> int()
    See rules on adventofcode.com, screw writing that again.
    """

    if part == 1:
        step_length = 1
    else:
        step_length = len(data)/2

    tot = 0
    max_len = len(data)

    for i in range(0, len(data)):
        compare_index = i+step_length
        if compare_index >= max_len:
            if data[i] == data[compare_index-max_len]:
                tot += int(data[i])
        elif data[i] == data[compare_index]:
            tot += int(data[i])

    return tot


def main():
    """ main()
    Reads input data from input_data.txt and feeds to decode. Prints result.
    Probably crashes a couple of times.
    """
    with open('input_data.txt', 'r') as in_data:
        print decode(in_data.read().strip(), 2)


if __name__ == '__main__':
    main()
