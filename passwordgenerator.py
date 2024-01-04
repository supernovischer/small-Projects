import random
import secrets
import string

"""
    Generate a random password of the specified length.

    :param length: The length of the password to generate.
    :type length: int
    :return: The randomly generated password.
    :rtype: str
"""
def generate_password(length):
    # Generate a random password of the specified length
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("Generated password:", generate_password(50))

"""
    Generates a random password of a specified length.

    Parameters:
        length (int): The length of the password. Default is 12.
        include_uppercase (bool): Whether or not to include uppercase letters in the password. Default is True.
        include_lowercase (bool): Whether or not to include lowercase letters in the password. Default is True.
        include_digits (bool): Whether or not to include digits in the password. Default is True.
        include_symbols (bool): Whether or not to include symbols in the password. Default is True.

    Returns:
        str: The randomly generated password.
"""
def generate_password(length=12, include_uppercase=True, include_lowercase=True, include_digits=True, include_symbols=True):
    characters = ""
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_digits:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

print("Generated password:", generate_password(50, True, True, False, False))
print("Generated password:", generate_password(50, True, True, True, False))
print("Generated password:", generate_password(50, True, True, True, True))