#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    argc = len(argv) - 1
    arg_str = "argument" if argc == 1 else "arguments"

    print("{} {}{}:".format(argc, arg_str, '.' if argc == 0 else ''))

    for i, arg in enumerate(argv[1:], start=1):
        print("{}: {}".format(i, arg))
