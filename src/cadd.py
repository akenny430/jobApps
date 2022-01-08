import argparse

from aux.cFunctions import addCompany

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-n', '--name', type=str, required=True, help='Name of company'
    )
    parser.add_argument(
        '-c', '--cid', type=str, required=True, help='ID used for company'
    )
    args = parser.parse_args()

    addCompany(args.name, args.cid)