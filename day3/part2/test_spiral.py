""" test_spiral.py
Verifies the implementation of the matrix generator for day 3 step 2
"""
import spiral


def test_preceeding_square_simple():
    """ test_preceeding_square_simple()
    Verify that the function returns the correct value square using the example
    from the excercise description.
    """
    expected = 4
    result = spiral.get_preceeding_square(5)

    assert expected == result


def test_preceeding_square_simple_1():
    """ test_preceeding_square_simple_2()
    Verify that the function returns the correct value square using the example
    from the excercise description.
    """
    expected = 23
    result = spiral.get_preceeding_square(25)

    assert expected == result


def test_preceeding_square_simple_2():
    """ test_preceeding_square_simple_2()
    Verify that the function returns the correct value square using the example
    from the excercise description.
    """
    expected = 133
    result = spiral.get_preceeding_square(141)

    assert expected == result


def test_calculate_value_1_0():
    """ test_calculate_value_1()
    Verify that the calculation of square values are done correctly
    """
    input_matrix = {
        (0, 0): 1,
        (1, 0): 1
    }
    expected = 2
    result = spiral.calculate_square_value(1, 1, input_matrix)

    assert expected == result


def test_calculate_value_minus_1_1():
    """ test_calculate_value_minus_1_1()
    Verify that the calculation of square values are done correctly
    """
    input_matrix = {
        (0, 0): 1,
        (1, 0): 1,
        (1, 1): 2,
        (0, 1): 4,
        (-1, 1): 5
    }
    expected = 5
    result = spiral.calculate_square_value(-1, 1, input_matrix)

    assert expected == result


def test_calculate_value_0_minus_1():
    """ test_calculate_value_0_minus_1()
    Verify that the calculation of square values are done correctly
    """
    input_matrix = {
        (0, 0): 1,
        (1, 0): 1,
        (1, 1): 2,
        (0, 1): 4,
        (-1, 1): 5,
        (-1, 0): 10,
        (-1, -1): 11
    }
    expected = 23
    result = spiral.calculate_square_value(0, -1, input_matrix)

    assert expected == result
