#!/usr/local/bin/python3

import re, sys
import string, os

DIR = '/Users/mac/Desktop/Climate Change Data/ABC' #sys.argv[1]

    
def splitFilesFromDir(top_directory):
    for root, dirs, files in os.walk(top_directory):
        for file in filter(lambda file: file.endswith('.TXT'), files):
            doc = open(os.path.join(root, file), encoding='utf8').read() # read the entire document, as one big string
            i = 0
            for article in re.split('\d+ of \d+ (DOCUMENTS|DOCUMENT)\s+ABC News Transcripts', doc):
                new_filename = file +'-' + str(i) + '.txt'
                new_file = open (os.path.join(root,new_filename), 'w')
                article = re.sub("Copyright \d+ American Broadcasting Companies, Inc.","",article)
                new_file.write(article)
                new_file.close()
                i = i + 1
            os.remove(os.path.join(root,file))
            os.remove(os.path.join(root,file + '-' + '0' + '.txt'))

if __name__ == "__main__":
    if len(sys.argv) == 1:
        splitFilesFromDir(DIR)
    else:
        splitFilesFromDir(sys.argv[1])






