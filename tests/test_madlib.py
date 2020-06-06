from madlib_cli.madlib import reading


def test_reading():
    actual = reading('assets/madlib.txt')
    expected = ''
    assert actual != expected


# def test_user_input():
#     actual = user_input(word)
#     expected = ''
#     assert actual != expected
