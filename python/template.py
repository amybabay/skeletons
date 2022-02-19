import sys, argparse

def get_args(argv):
    parser = argparse.ArgumentParser(description="Description")
    parser.add_argument('-s', '--string-arg', required=False, default="test")
    parser.add_argument('-i', '--int-arg', required=False, default=1, type=int)
    return parser.parse_args()

def main(argv):
    args = get_args(argv)

    print(args.string_arg)
    print(args.int_arg)

if __name__ == "__main__":
    main(sys.argv[1:])
