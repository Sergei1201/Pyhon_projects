import sys
import hashlib
import requests

# Check API URL


def check_api_url(query_string):
    url = 'https://api.pwnedpasswords.com/range/' + query_string
    res = requests.get(url)
    # Check the response
    if res.status_code != 200:
        raise RuntimeError(
            f'Response error {res.status.code}. Check the URL and try again')
    return res


# Password leakage function
def pass_hack_count(hashes, hash_to_compare):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_compare:
            return count
    return 0

# Password checker function


def pass_hash(password):
    # Hash password
    hash_sha1 = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    # Split the hash
    first5_chars, tail = hash_sha1[:5], hash_sha1[5:]
    # Get response
    response = check_api_url(first5_chars)
    # Call password leakage function
    return pass_hack_count(response, tail)


# Main function
def main(args):
    for password in args:
        count = pass_hash(password)
        if count:
            print(
                f'The password {password} has been hacked {count} times. You should try another password')
        else:
            print(f'The password {password} has never been hacked. Good job')
    return 'done'


if __name__ == '__main__':
    main(sys.argv[1:])
