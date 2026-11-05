import re


def is_valid_email(email):
    return bool(re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email or ""))


def is_strong_password(pw):
    pw = pw or ""
    return len(pw) >= 8 and any(c.isdigit() for c in pw) and any(c.isupper() for c in pw)
