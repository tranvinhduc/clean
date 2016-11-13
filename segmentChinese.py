#!/usr/local/bin/python3

import re, sys
import string, os
import jieba

    
def splitFilesFromDir(top_directory):
    for root, dirs, files in os.walk(top_directory):
        for file in filter(lambda file: file.endswith('.txt'), files):
            doc = open(os.path.join(root, file), encoding='utf8').read() # read the entire documentls, as one big string
            seg_list = jieba.cut(doc,cut_all=False)
            new_filename = file
            new_file = open (os.path.join(root,new_filename), 'w')
            new_file.write(" ".join(seg_list))
            new_file.close()
            #     i = i + 1
            # os.remove(os.path.join(root,file))
            # os.remove(os.path.join(root,file + '-' + str(i-1) + '.txt'))

if __name__ == "__main__":
    jieba.set_dictionary('data/dict.txt.big')
    jieba.initialize()  # (optional)
    if len(sys.argv) == 1:
        print('Usage: '+ sys.argv[0] + ' DIR')
    else:
        splitFilesFromDir(sys.argv[1])






