def normalize_email(email: str) -> str:
    return email.strip().lower()

def test_normalize_email():
    assert normalize_email(" USER@EXAMPLE.COM ") == "user@example.com"
