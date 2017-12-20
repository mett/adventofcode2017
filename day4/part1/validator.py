""" validator.py
Validate passwords. They should be a series of words separated by spaces. A
valid password should contain no duplicate words.
"""


def is_valid(input_string):
    """ is_valid(input_string) -> bool()
    Returns True or False depending on if a password is valid.
    """
    tokens = input_string.split()

    for word in tokens:
        if tokens.count(word) > 1:
            return False
    return True


def main():
    """ main()
    Print number of valid passwords in input.txt
    """
    count = 0
    with open('input.txt') as input_file:
        for line in input_file:
            if is_valid(line):
                count += 1
            else:
                print line
    print count


if __name__ == '__main__':
    main()
