from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("3/4") == 75

def test_non_digits():
    with pytest.raises(ValueError):
        assert convert("cat/dog")
        assert convert("cat")

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        assert convert("9/0")

def test_gauge():
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(75) == "75%"
