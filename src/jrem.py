import argparse

from aux.jFunctions import removeJob

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'cid', type=str, help='ID used for company'
    )
    parser.add_argument(
        'jid', type=str, help='ID used for job'
    )
    args = parser.parse_args()

    removeJob(args.cid, args.jid)