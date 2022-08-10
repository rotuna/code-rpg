def is_valid(user_input: str, valid: set[str]) -> bool:
    if user_input in valid:
        return True
    else:
        return False
