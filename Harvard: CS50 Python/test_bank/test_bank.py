from bank import value

def test_short():
    assert value("Hello") == 0

def test_ish():
    assert value("hi, iam") == 20

def test_yolo():
    assert value("cobra") == 100
