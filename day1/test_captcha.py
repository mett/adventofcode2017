""" test_captcha
Verify decode function for day 1 of Advent of Code
"""
import captcha


def test_1122_3():
    """ test_1122_3
    Input: 1122
    Output: 3
    """
    expected = 3
    stimuli = '1122'

    result = captcha.decode(stimuli)

    assert expected == result


def test_1111_4():
    """ test_1111_4
    Input: 1111
    Output: 4
    """
    expected = 4
    stimuli = '1111'

    result = captcha.decode(stimuli)

    assert expected == result


def test_1234_0():
    """ test_1234_0
    Input: 1234
    Output: 0
    """
    expected = 0
    stimuli = '1234'

    result = captcha.decode(stimuli)

    assert expected == result


def test_91212129_9():
    """ test_91212129_9()
    Input: 91212129
    Output: 9
    """
    expected = 9
    stimuli = '91212129'

    result = captcha.decode(stimuli)

    assert expected == result


def test_1212_6():
    """ test_1212_6()
    Input: 1212
    Output: 6
    """
    expected = 6
    stimuli = '1212'

    result = captcha.decode(stimuli, part=2)

    assert expected == result


def test_123425_4():
    """ test_123425_4()
    Input: 123425_4
    Output: 4
    """
    expected = 4
    stimuli = '123425'

    result = captcha.decode(stimuli, part=2)

    assert expected == result


def test_123123_12():
    """ test_123123_12()
    Input: 123123
    Output: 12
    """
    expected = 12
    stimuli = '123123'

    result = captcha.decode(stimuli, part=2)

    assert expected == result


def test_12131415_4():
    """ test_12131415_4()
    Input: 12131415
    Output: 4
    """
    expected = 4
    stimuli = '12131415'

    result = captcha.decode(stimuli, part=2)

    assert expected == result
