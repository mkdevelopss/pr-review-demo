from validators import is_valid_email, is_strong_password


def test_email():
    assert is_valid_email("a@b.com")
    assert not is_valid_email("ab.com")
    assert not is_valid_email("a@bcom")
    assert not is_valid_email("a@@b.com")


def test_password():
    assert is_strong_password("Abcdefg1")
    assert not is_strong_password("abcdefg1")   # no uppercase
    assert not is_strong_password("Abcdefgh")   # no digit
    assert not is_strong_password("Ab1")        # too short
