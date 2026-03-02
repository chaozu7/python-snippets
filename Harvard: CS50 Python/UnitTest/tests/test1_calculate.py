from calculate import square
import pytest

def tests_positive():
    assert square(2) == 4
    assert square(3) == 9
    
#pytest

def test_negatives():
    assert square(-2) == 4
    assert square(-3) == 9
    
def test_zero():
    assert square(0) == 0
    
    
def test_str():
    with pytest.raises(TypeError):
        square("cat")