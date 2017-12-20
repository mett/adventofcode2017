""" test_validator.py
Verify the password validator, day 4 of advent of code.
"""
import validator


def test_validator_simple_1():
    """ test_validator_simple_1()
    Verify that we pass the simple use cases.
    """
    input_string = 'aa bb cc dd ee'
    expected = True
    result = validator.is_valid(input_string)

    assert expected == result


def test_validator_simple_2():
    """ test_validator_simple_2()
    Verify that we pass the simple use cases.
    """
    input_string = 'aa bb cc dd aa'
    expected = False
    result = validator.is_valid(input_string)

    assert expected == result


def test_validator_simple_3():
    """ test_validator_simple_3()
    Verify that we pass the simple use cases.
    """
    input_string = 'aa bb cc dd aaa'
    expected = True
    result = validator.is_valid(input_string)

    assert expected == result


def test_validator_simple_4():
    """ test_validator_simple_4()
    Verify that we pass the simple use cases.
    """
    input_string = 'aa aa cc dd'
    expected = False
    result = validator.is_valid(input_string)

    assert expected == result
