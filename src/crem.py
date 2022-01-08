import argparse

from aux.cFunctions import removeCompany

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-c', '--cid', type=str, required=True, help='ID used for company'
    )
    args = parser.parse_args()

    removeCompany(args.cid)