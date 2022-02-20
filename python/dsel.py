#!/usr/bin/env python3 
import argparse 

from aux.dfun import selectData

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'name', type=str, help='Name of dataset you want to remove'
    )
    args = parser.parse_args()

    selectData(args.name)