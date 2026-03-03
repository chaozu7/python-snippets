from twttr import shorten

def test_string():
    assert shorten("kamila") == "kml"

def test_only():
    assert shorten("oae") == ""

def test_cap():
    assert shorten("kAtO") == "kt"

def test_numb():
    assert shorten("k2o") == "k2"

def test_punkt():
    assert shorten("K.am") == "K.m"



