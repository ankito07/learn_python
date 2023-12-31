import requests
import hashlib
import re

"""This is not just a simple password checker in this project we will build a password_checker that tells you that
the password you have created has ever been hacked or not along with its count."""


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
    return res


def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)


def is_valid_password(password):
    # Check length (at least 8 characters)
    if len(password) < 8:
        return False

    # Check if it contains at least one lowercase letter
    if not re.search(r'[a-z]', password):
        return False

    # Check if it contains at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        return False

    # Check if it contains at least one digit
    if not re.search(r'\d', password):
        return False

    # Check if it contains at least one special character
    if not re.search(r'[@#$%^&*!]', password):
        return False

    return True


def main(password):
    if is_valid_password(password):
        print("Password is valid.")
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times... you should probably change your password!')
        else:
            print(f'{password} was NOT found. Carry on!')
    else:
        print("Password is invalid. Please make sure it has at least 8 characters, "
              "including at least one lowercase letter, one uppercase letter, one digit, "
              "and one special character (@#$%^&*!).")


if __name__ == '__main__':
    password_check = input("Please enter your password: ")
    main(password_check)


