from email_validator import validate_email, EmailNotValidError


def check_email(email: str) -> bool:
    try:
        v = validate_email(email)
        email = v['email']
        return True
    except EmailNotValidError:
        return False