from seasons import convert

def test_minutes():
    assert convert(1) == "One thousand, four hundred forty minutes"
    assert convert(12817) == "Eighteen million, four hundred fifty-six thousand, four hundred eighty minutes"

