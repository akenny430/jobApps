import argparse

from aux.pFunctions import printInfo

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # parser.add_argument(
    #     '-c', '--cid', type=str, default=None, help='ID of company to specify'
    # )
    parser.add_argument(
        'cid', type=str, nargs = '?', default=None, help='ID of company to specify'
    )
    parser.add_argument(
        '-l', '--level', action='count', help='Level of detail used when printing'
    )
    parser.add_argument(
        '-p', '--personal', action='store_true', help='Specify whether or not to print personal info'
    )
    args = parser.parse_args()

    # if no level is supplied, then we set it to 3, otherwise each additional tag adds a level (starts with 2)
    # so can have either -l or -ll, and default is -ll
    # (better way to do this?)
    if args.level is None:
        if args.cid is None:
            defLevel = 3
        else:
            defLevel = 1
    else:
        defLevel = int(args.level)

    printInfo(args.cid, defLevel, args.personal) 
    # print(args)