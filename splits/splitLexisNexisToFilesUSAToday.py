#!/usr/local/bin/python3

import re, sys
import string, os


    
def splitFilesFromDir(top_directory):
    DateCut=re.compile(r'(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d+,\s+\d+.*(\s+Late Edition - Final)?(\s+FINAL EDITION)?')
    BylineCut=re.compile(r'BYLINE:.*')
    TypeCut=re.compile(r'TYPE:.*')
    Dateline=re.compile(r'DATELINE:.*')
    SectionCut=re.compile(r'SECTION:.*')
    LengthCut=re.compile(r'LENGTH:.*')
    LanguageCut=re.compile(r'LANGUAGE:.*')
    PublicationTypeCut=re.compile(r'PUBLICATION-TYPE:.*')
    DocumentTypeCut=re.compile(r'DOCUMENT-TYPE:.*')
    LoadDateCut=re.compile(r'LOAD-DATE:.*')
    UrlCut=re.compile(r'URL:.*\n\n',re.DOTALL)                                        #Attention: cut all to the end!!!!! Assume that: URL is in the end
    HttpCut=re.compile(r'http:.*')
    GraphicCut=re.compile(r'GRAPHIC:.*$',re.DOTALL)
    NYTCut = re.compile(r'The New York Times Blogs')
    NYTCut2 = re.compile(r'.Dot Earth.\n\n')
    for root, dirs, files in os.walk(top_directory):
        for file in filter(lambda file: file.endswith('.TXT'), files):
            doc = open(os.path.join(root, file), encoding='utf8').read() # read the entire documentls, as one big string
            doc = re.sub(r"Copyright \d+ Gannett Company Inc.","",doc)
           # doc = re.sub(r"Copyright \d+ The New York Times Company(\s+All Rights Reserved)?","",doc)
           # doc = NYTCut.sub("", doc)
   #         doc = NYTCut2.sub("", doc)
            doc = DateCut.sub('',doc)
            doc = BylineCut.sub("",doc)
            doc = Dateline.sub("",doc)
            doc = SectionCut.sub("",doc)
            doc = LengthCut.sub("",doc)
            doc = LanguageCut.sub("",doc)
            doc = PublicationTypeCut.sub("",doc)
            doc = DocumentTypeCut.sub("",doc)
            doc = LoadDateCut.sub("",doc)
            doc = TypeCut.sub("",doc)

            i = 0
            for article in re.split('\d+ of \d+ DOCUMENTS\s+USA TODAY.*', doc):
                new_filename = file +'-' + str(i) + '.txt'
                new_file = open (os.path.join(root,new_filename), 'w')
                #  article = NYTCut.sub("", article)
                article = NYTCut2.sub("", article)
                article = UrlCut.sub('',article)
                article = HttpCut.sub('',article)
                article = GraphicCut.sub('',article)
                new_file.write(article)
                new_file.close()
                i = i + 1
            os.remove(os.path.join(root,file))
            os.remove(os.path.join(root,file + '-' + '0' + '.txt'))

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print('Usage: '+ sys.argv[0] + ' LexisNexis-directory')
    else:
        splitFilesFromDir(sys.argv[1])






