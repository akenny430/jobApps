import argparse

from aux.jFunctions import addJob

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-c', '--cid', type=str, required=True, help='ID used for company'
    )
    parser.add_argument(
        '-n', '--name', type=str, required=True, help='Name of job applying'
    )
    parser.add_argument(
        '-j', '--jid', type=str, default=None, help='ID used for job'
    )
    parser.add_argument(
        '-d', '--date', type=str, default=None, help='Date applied to job'
    )
    args = parser.parse_args()

    addJob(args.cid, args.name, args.jid, args.date)