##!/usr/local/bin/python3

import re, sys
import string, os
import subprocess

DIR = 'home/tran/Projects/TopicsModelling/Columbia/' #sys.argv[1]
def readDir(top_directory):
    for root, dirs, files in os.walk(top_directory):
        for file in filter(lambda file: file.endswith('.pdf'), files):
            subprocess.run (['java', '-jar', '/home/tran/bin/pdfbox-app-2.0.0.jar', 'ExtractText',os.path.join(root,file), os.path.join(root,file)+'.txt'])
            print (os.path.join(root,file))
            os.remove(os.path.join(root,file))


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print('Usage: '+ sys.argv[0] + ' LexisNexis-directory')
    else:
        readDir(sys.argv[1])

# bigfile = open(filename, 'r')
# bigstring = bigfile.read()
#
# i = 0
# for article in re.split('\d+ of \d+ DOCUMENTS',bigstring):
#     new_filename = filename_ +'-' + str(i) + '.txt'
#     new_file = open (new_filename, 'w')
#     new_file.write(article)
#     new_file.close()
#     i = i + 1





