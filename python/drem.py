#!/usr/bin/env python3 
import argparse

from aux.dfun import removeData

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'name', type=str, help='Name of dataset to remove'
    )
    parser.add_argument(
        '-d', '--default', type=str, default=None, help='Name of new default dataset'
    )
    args = parser.parse_args()

    removeData(args.name, args.default)