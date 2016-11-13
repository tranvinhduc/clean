#!/usr/local/bin/python3

import re, sys
import string, os


def splitFilesFromDir(top_directory, pattern):
    for root, dirs, files in os.walk(top_directory):
        for file in filter(lambda file: file.endswith('.TXT'), files):
            doc = open(os.path.join(root, file), encoding='utf8').read()
            # read the entire documentls, as one big string
            i = 0
            for article in re.split(pattern, doc):
                #for article in re.split('Document NACCHL.*', doc):
                new_filename = file + '-' + str(i) + '.txt'
                new_file = open(os.path.join(root, new_filename), 'w')
                # article = NYTCut.sub("", article)
                # article = ABCCut.sub('', article)
                # article = UrlCut.sub('',article)
                # article = HttpCut.sub('',article)
                # article = GraphicCut.sub('',article)
                new_file.write(article)
                new_file.close()
                i = i + 1
            os.remove(os.path.join(root, file))
            os.remove(os.path.join(root, file + '-' + '0' + '.txt'))

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print('Usage: ' + sys.argv[0] + ' LexisNexis-directory')
    else:
        splitFilesFromDir(sys.argv[1],'\d+ of \d+ DOCUMENTS')

#        splitFilesFromDir(sys.argv[1], 'Die Presse vom \d+-\d+-\d+, Seite: \d+\n\n')

        #splitFilesFromDir(sys.argv[1], '\"Der Standard\" vom \d+\.\d+\.\d+\s+Seite: \d+\n\n')

        #splitFilesFromDir(sys.argv[1], '\"Kronen Zeitung\" vom \d+\.\d+\.\d+\s+Seite: \d+\n\n')

#        splitFilesFromDir(sys.argv[1], 'Blick vom \d+.\d+\.\d+ Seite .\d+\n\n')

        #splitFilesFromDir(sys.argv[1], '\nNeue Zürcher Zeitung \d+\.\d+\.\d+.*\n\n')
        #splitFilesFromDir(sys.argv[1], '\nTagesanzeiger vom \d+\.\d+\.\d+ Seite.*\n\n')
        #splitFilesFromDir(sys.argv[1], '\nNZZ am Sonntag \d+\.\d+\.\d+.*\n\n')

#        splitFilesFromDir(sys.argv[1], '\nSonntagsblick vom \d+\.\d+\.\d+.*\n\n')


#        splitFilesFromDir(sys.argv[1], r'Quelle(\n.*){1,10}© GBI-Genios Deutsche Wirtschaftsdatenbank GmbH(\s|\n)*$')

# Tagesanzeiger vom \d+\.\d+\.\d+ Seite\s+\d+\s+/.*\n.*')

