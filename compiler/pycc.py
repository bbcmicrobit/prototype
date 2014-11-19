#!/usr/bin/python

import sys
from py2cc.main import main_single

def single_usage(prog):

    print "Usage:"
    print
    print prog, "source/filename.py dest/filename.hex build_directory"

if __name__ == "__main__":
    if len(sys.argv) <4:
        single_usage(prog)
        sys.exit(1)

    prog = sys.argv[0]
    source_file = sys.argv[1]
    dest_file = sys.argv[2]
    build_directory = sys.argv[3]

    main_single(source_file, dest_file, build_directory)