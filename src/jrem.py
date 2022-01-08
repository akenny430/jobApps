import argparse

from aux.jFunctions import removeJob

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-c', '--cid', type=str, required=True, help='ID used for company'
    )
    parser.add_argument(
        '-j', '--jid', type=str, required=True, help='ID used for job'
    )
    args = parser.parse_args()

    removeJob(args.cid, args.jid)