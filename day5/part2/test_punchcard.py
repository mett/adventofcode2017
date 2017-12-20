""" test_punchcard.py
Verify implementation of punchcard
"""
import punchcard


def test_punchcard():
    input_instructions = [0, 3, 0, 1, -3]
    expected = 10

    result = punchcard.run(input_instructions)
    assert expected == result
