#!/usr/local/bin/python3

import re, sys
import string, os,shutil


    
def splitFilesFromDir(top_directory):
    #DateCut=re.compile(r'(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d+,\s+\d+.*(\s+Late Edition - Final)?')
    last6months = ['Jul','Aug', 'Sep','Oct', 'Nov', 'Dec']
    for root, dirs, files in os.walk(top_directory):
        if not os.path.exists(root+"-2"):
            os.makedirs(root+"-2")
        for file in filter(lambda file: file.endswith('.txt'), files):
            if file[16:19] in last6months:
                print ("mv "+ os.path.join(root,file) + " "+ root+"-2")
                shutil.move(os.path.join(root,file), root+"-2")
            # doc = open(os.path.join(root, file), encoding='utf8').read() # read the entire documentls, as one big string
           
            # os.remove(os.path.join(root,file))
            # os.remove(os.path.join(root,file + '-' + '0' + '.txt'))

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print('Usage: '+ sys.argv[0] + ' LexisNexis-directory')
    else:
        splitFilesFromDir(sys.argv[1])






