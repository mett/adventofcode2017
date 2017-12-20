""" test_spiral.py
Tests to verify the implementation of day 3.
"""
import spiral


def test_spiral_generation_9():
    """ test_spiral_generation_9()
    Should correctly generate the spiral matrix up to the 9th position.
    """
    expected = [
        (0, 0),
        (1, 0),
        (1, 1),
        (0, 1),
        (-1, 1),
        (-1, 0),
        (-1, -1),
        (0, -1),
        (1, -1)
    ]
    result = spiral.generate(9)
    assert expected == result


def test_spiral_generation_3():
    """ test_spiral_generation_3()
    Should correctly generate the spiral matrix up to the 9th position.
    """
    expected = [
        (0, 0),
        (1, 0),
        (1, 1)
    ]
    result = spiral.generate(3)
    assert expected == result


def test_calculate_distance_12():
    """ test_calculate_distance_12()
    Check that we calculate the length to 12 correctly
    """
    expected = 3
    result = spiral.steps_to(12)

    assert expected == result


def test_calculate_distance_23():
    """ test_calculate_distance_12()
    Check that we calculate the length to 12 correctly
    """
    expected = 2
    result = spiral.steps_to(23)

    assert expected == result


def test_calculate_distance_1024():
    """ test_calculate_distance_1024()
    Check that we calculate the length to 12 correctly
    """
    expected = 31
    result = spiral.steps_to(1024)

    assert expected == result
