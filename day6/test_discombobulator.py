""" test_discombobulator.py
Verify implementation of the discombobulator
"""
import discombobulator


def test_basic_scenario():
    """ test_basic_scenario()
    Verify that we pass the instructions given in the exercise description
    """
    membank = [0, 2, 7, 0]
    expected = 5

    result = discombobulator.shake(membank)

    assert expected == result
