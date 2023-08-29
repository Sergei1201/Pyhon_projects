import requests
import sys
import hashlib

# Check URL API


def check_url_api(query_string):
    url = f'https://api.pwnedpasswords.com/range/{query_string}'
    res = requests.get(url)
    # Check if the status code is not equal to 200. If so, raise an error, otherwise return response
    if res.status_code != 200:
        raise RuntimeError(
            f'Response error {res.status_code}. Check the URL and try again')
    return res

# Check how many times the password has been hacked


def hack_pass_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


# Check the password
def check_pass(password):
    # Hash password with SHA1
    hash_sha1 = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    # Get first 5 characters of the hash and the rest
    first5_chars, tail = hash_sha1[:5], hash_sha1[5:]
    # Pass the first 5 characters of the hash to check_url_api function
    response = check_url_api(first5_chars)
    return hack_pass_count(response, tail)


def main(args):
    for password in args:
        count = check_pass(password)
        if count:
            print(
                f'Your password has been hacked {count} times. You should enter another password')
        else:
            print(f'Your password has never been hacked. Good job')
    return 'done'


if __name__ == '__main__':
    main(sys.argv[1:])
