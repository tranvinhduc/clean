#!/usr/local/bin/python3

import re, sys
import string, os


def removeShortDocFromDir(top_directory, length):
    for root, dirs, files in os.walk(top_directory):
        for file in filter(lambda file: file.endswith('.txt'), files):
            doc = open(os.path.join(root, file), encoding='utf8').read()
            if len(doc) < length:
                os.remove(os.path.join(root, file))

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print('Usage: ' + sys.argv[0] + ' length')
    else:
        removeShortDocFromDir(sys.argv[1], int(sys.argv[2]))
