""" test_balance.py
Verify the tree balancing implementation for day 7 of advent of code.
"""
import balance


def test_tree_balace_root():
    """ test_tree_balace_root()
    Verify that we correctly identify the root of the tree
    """
    result = balance.generate_tree('test_input.txt')
    expected = 'tknk'

    assert expected == result['root'][0]
