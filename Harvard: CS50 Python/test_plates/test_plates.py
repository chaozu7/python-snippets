from plates import is_valid

def test_limit():
    assert is_valid("Kokokokokok") == False

def test_number():
    assert is_valid("Koj87j") == False

def test_char():
    assert is_valid("Kok,.") == False

def test_isnumberzero():
    assert is_valid("Kok0") == False

def test_limit_char():
    assert is_valid("ll8k6k") == False

def test_is_too_short():
    assert is_valid("K") == False

def test_alpha():
    assert is_valid("&--+kkKojo") == False


def test_numb():
    assert is_valid("33") == False
