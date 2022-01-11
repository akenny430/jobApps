#!/usr/bin/env python3
import argparse

from aux.cfun import removeCompany

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'cid', type=str, help='ID used for company'
    )
    args = parser.parse_args()

    removeCompany(args.cid)