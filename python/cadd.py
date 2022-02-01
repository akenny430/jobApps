#!/usr/bin/env python3
import argparse

from aux.cfun import addCompany

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'name', type=str, help='Name of company'
    )
    parser.add_argument(
        'cid', type=str, help='ID used for company'
    )
    args = parser.parse_args()

    addCompany(args.name, args.cid)