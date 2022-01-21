#!/usr/bin/env python3
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(
        description='login to IMAP and search for email')
    parser.add_argument(
        '--host', type=str, help='IMAP hostname: imap.domain.com', metavar='')
    parser.add_argument(
        '--user', type=str, help='Username', metavar='')
    parser.add_argument(
        '--pass', type=str, help='Password', metavar='')
    parser.add_argument(
        '--debug', help='Debug this script', action='store_true')

    global args
    args = parser.parse_args()

    return 0

if __name__ == '__main__':
    sys.exit(main())