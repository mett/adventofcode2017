""" test_validator.py
Validate part2 of day 4. Anagram passwords.
"""
import validator


def test_validate_1():
    """ test_validate_1()
    Verify that we correctly verify passwords correctly according to step 2
    rules
    """
    input_string = 'abcde fghij'
    result = validator.verify(input_string)

    assert result


def test_validate_2():
    """ test_validate_2()
    Verify that we correctly verify passwords correctly according to step 2
    rules
    """
    input_string = 'abcde xyz ecdab'
    result = validator.verify(input_string)

    assert not result


def test_validate_3():
    """ test_validate_3()
    Verify that we correctly verify passwords correctly according to step 2
    rules
    """
    input_string = 'a ab abc abd abf abj'
    result = validator.verify(input_string)

    assert result


def test_validate_4():
    """ test_validate_4()
    Verify that we correctly verify passwords correctly according to step 2
    rules
    """
    input_string = 'iiii oiii ooii oooi oooo'
    result = validator.verify(input_string)

    assert result


def test_validate_5():
    """ test_validate_5()
    Verify that we correctly verify passwords correctly according to step 2
    rules
    """
    input_string = 'oiii ioii iioi iiio'
    result = validator.verify(input_string)

    assert not result
