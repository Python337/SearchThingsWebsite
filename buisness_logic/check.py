def check_login(login: str) -> bool:
    if 5 <= len(login) <= 70:
        return True
    return False


def check_password(password: str) -> bool:
    if 10 <= len(password) <= 85:
        return True
    return False