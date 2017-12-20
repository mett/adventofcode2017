""" validator.py
Solution for Advent of code day 4
"""


def verify(input_string):
    """ verify(input_string) -> boolean()
    Verify password according to day 4 part 2 rules. No anagrams
    """
    words = input_string.split()
    sorted_words = []

    for word in words:
        l_word = list(word)
        l_word.sort()
        if l_word not in sorted_words:
            sorted_words.append(l_word)
        else:
            return False
    return True


def main():
    """ main()
    Print number of valid passwords in input.txt
    """
    count = 0
    with open('input.txt') as input_file:
        for line in input_file:
            if verify(line):
                count += 1
            else:
                print line
    print count


if __name__ == '__main__':
    main()
