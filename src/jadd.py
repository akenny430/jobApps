import argparse

from aux.jfun import addJob

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'cid', type=str, help='ID used for company'
    )
    parser.add_argument(
        'name', type=str, help='Name of job applying'
    )
    parser.add_argument(
        'jid', type=str, nargs='?', default=None, help='ID used for job'
    )
    parser.add_argument(
        '-d', '--date', type=str, default=None, help='Date applied to job'
    )
    args = parser.parse_args()

    addJob(args.cid, args.name, args.jid, args.date)