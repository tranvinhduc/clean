#!/usr/local/bin/python3

import re, sys
import string, os

#string = r'^[\n\s]*SEVILLA Edición'
#string = r'All Rights Reserved[\n\s]*$'
#string = r'Copyright ©.*\n.*\n.*\n(.*\n\n)?'
#string = r'Copyright Grupo.*\n.*\n.*\n(.*\n\n)?'
#string = r'\n\s{10,60}.{1,60}\n'
#string = r'\s{10,60}.{1,40}\n'
#string = r'\s{10,60}.{1,60}Edición\n'
#string = r'.*\n\s*All Rights Reserved[\n\s]*$'
#string = r'\n\n[A-Z\-]{1,30}:.{0,100}'


#string = r'Classification:.*'
string = r'\n[A-Z\-]{1,50}:.*'

#string = r'^\n\s*.*\n{1,3}\s*(January|February|March|April|May|June|July|August|September|October|November|December|JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER) \d+, \d+.*\n\n'


#string = r'^\n\s*.*\n{1,3}\s*(January|February|March|April|May|June|July|August|September|October|November|December|JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER) \d+, \d+.*\n\s*.*Edition\n\n'


#string = r'\nFor Reprint Rights: timescontent\.com'
#string = r'^[\s\n]*(January|February|March|April|May|June|July|August|September|October|November|December|JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER) \d+, \d+.*\n\n'

#string = r'Published by HT.*\n.*\n.*htsyndication@hindustantimes\.com[\n\s]{0,100}$'

#string = r'^[\s\n]*.*[\s\n]*(January|February|March|April|May|June|July|August|September|October|November|December|JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER) \d+, \d+.*\n.*\n.*Edition\n\n'

#string = r'^\n*\s*The New York Times\n\n.*\n.*\n\n'


#string = r'^\n*\s*USA TODAY\n{1,3}\s{10,30}.*\n{1,3}\s{10,30}.*(\n{1,3}\s{10,30}.*)?\n'

#string = r'\s{10,100}Copyright.*\n\s{10,100}All Rights Reserved[\n\s]*$'
def splitFilesFromDir(top_directory, pattern):
    p = re.compile(pattern)
    i = 0
    for root, dirs, files in os.walk(top_directory):
        for file in filter(lambda file: file.endswith('.txt'), files):
            file1 = open(os.path.join(root, file),  encoding='utf8')
            # read the entire documentls, as one big string
            doc = file1.read()
            file1.close()
            file1 = open(os.path.join(root, file), 'w', encoding='utf8')
            doc = p.sub("", doc)
            file1.write(doc)
            i = i + 1
            file1.close()
    print('So file thay the ', i)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print('Usage: ' + sys.argv[0] + ' <replaced directory>' + ' <regular expression>')
    else:
#        splitFilesFromDir(sys.argv[1], r'Quelle(\n|.){1,500}GBI-Genios Deutsche Wirtschaftsdatenbank GmbH')

#        splitFilesFromDir(sys.argv[1], r'Quelle(\n|.){1,500}GBI-Genios Deutsche Wirtschaftsdatenbank GmbH')
        
        splitFilesFromDir(sys.argv[1], string)
