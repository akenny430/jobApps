import argparse

from aux.jFunctions import updateJob

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-c', '--cid', type=str, required=True, help='ID used for company'
    )
    parser.add_argument(
        '-j', '--jid', type=str, required=True, help='ID used for job'
    )
    parser.add_argument(
        '-m', '--message', type=str, required=True, help='ID used for job'
    )
    parser.add_argument(
        '-r', '--rejected', action='store_true', help='Flag to indicate rejection'
    )
    parser.add_argument(
        '-o', '--offered', action='store_true', help='Flag to indicate offer'
    )
    parser.add_argument(
        '-a', '--accepted', action='store_true', help='Flag to indicate acceptance'
    )
    parser.add_argument(
        '-w', '--waiting', action='store_true', help='Flag to indicate waiting (if we are rejected but then reconsidered'
    )
    args = parser.parse_args()

    if args.rejected is True: 
        updateFlag = 'r'
    elif args.offered is True: 
        updateFlag = 'o'
    elif args.accepted is True: 
        updateFlag = 'a'
    elif args.waiting is True: 
        updateFlag = 'w'
    else: 
        updateFlag = None
    updateJob(args.cid, args.jid, args.message, updateFlag)