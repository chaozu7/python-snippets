from um import count

def test_uppercase_text():
    assert count("this is UM and um")== 2
    assert count("UM UM UM") == 3

def test_no_value():
    assert count("jo") == 0
    assert count("jestum") == 0

def test_value_sign():
    assert count("um?") == 1
    assert count("Um! um? um") == 3


