from numb3rs import validate

def test_correct_ip():
        assert validate("134.132.45.254") == True


def test_wrong_ip():
        assert validate("IPv4 Address: 134.700.45.a") == False

def test_wrong_start_ip():
        assert validate("134.32.450.88") == False
        assert validate("134.700.67.188") == False
        assert validate("334.70.45.88") == False
        assert validate("134.70.67.883") == False

def test_too_short_ip():
        assert validate("IPv4 Address: 134.a.88") == False
        assert validate("IPv4 Address: 134.88") == False
        assert validate("IPv4 Address: 88") == False
        assert validate("IPv4 Address: 88.22.32.1.2") == False

