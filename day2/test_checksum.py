""" test_checksum.py
Collection of tests to verify day 2 of adventofcode.com
"""
import checksum


def test_row_even_division_1():
    """ test_row_even_division_1()
    Input: [5, 9, 2, 8]
    Expected: 4
    """
    stimuli = [5, 9, 2, 8]
    expected = 4

    result = checksum.calculate_row_even_div(stimuli)
    assert expected == result


def test_row_even_division_2():
    """ test_row_even_division_2()
    Input: [9, 4, 7, 3]
    Expected: 3
    """
    stimuli = [9, 4, 7, 3]
    expected = 3

    result = checksum.calculate_row_even_div(stimuli)
    assert expected == result


def test_row_even_division_3():
    """ test_row_even_division_2()
    Input: [3, 8, 6, 5]
    Expected: 2
    """
    stimuli = [3, 8, 6, 5]
    expected = 2

    result = checksum.calculate_row_even_div(stimuli)
    assert expected == result


def test_calculate_div_checksum():
    """ test_calculate_div_checksum()
    Input: [[5, 9, 2, 8],
            [9, 4, 7, 3],
            [3, 8, 6, 5]]
    Expected: 9
    """
    stimuli = [[5, 9, 2, 8],
               [9, 4, 7, 3],
               [3, 8, 6, 5]]
    expected = 9

    result = checksum.calculate_division_checksum(stimuli)
    assert expected == result


def test_spreadsheet_checksum():
    """ test_spreadsheet_checksum()
    Input: [[5, 1, 9, 5],
            [7, 5, 3],
            [2, 4, 6, 8]]
    Expected: 18
    """
    stimuli = [[5, 1, 9, 5],
               [7, 5, 3],
               [2, 4, 6, 8]]
    expected = 18

    result = checksum.calculate_min_max_checksum(stimuli)
    assert expected == result


def test_row_calculation_1():
    """ test_row_calculation_1()
    Input: [5, 1, 9, 5]
    Expected: 8
    """
    stimuli = [5, 1, 9, 5]
    expected = 8

    result = checksum.calculate_row_min_max(stimuli)
    assert expected == result


def test_row_calculation_2():
    """ test_row_calculation_2()
    Input: [7, 5, 3]
    Expected: 4
    """
    stimuli = [7, 5, 3]
    expected = 4

    result = checksum.calculate_row_min_max(stimuli)
    assert expected == result


def test_row_calculation_3():
    """ test_row_calculation_3()
    Input: [2, 4, 6, 8]
    Expected: 6
    """
    stimuli = [2, 4, 6, 8]
    expected = 6

    result = checksum.calculate_row_min_max(stimuli)
    assert expected == result
