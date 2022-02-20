#!/usr/bin/env python3 
import argparse

from aux.dfun import newData

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'name', type=str, help='Name of dataset to create'
    )
    parser.add_argument(
        '-e', '--email', type=str, default=None, help='Email for dataset'
    )
    parser.add_argument(
        '-p', '--phone', type=str, default=None, help='Phone number for dataset'
    )
    parser.add_argument(
        '-g', '--github', type=str, default=None, help='Link to GitHub account'
    )
    parser.add_argument(
        '-l', '--linkedin', type=str, default=None, help='Link to LinkedIn account'
    )
    parser.add_argument(
        '-t', '--twitter', type=str, default=None, help='Link to Twitter account'
    )
    args = parser.parse_args()

    newData(args.name, args.email, args.phone, args.github, args.linkedin, args.twitter)