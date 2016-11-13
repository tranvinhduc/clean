#!/bin/zsh

for file in *.TXT; do
    mkdir  ${file:21:6}   #lay mot phan cua file tu 9 (tinh tu 0), keo dai 6 ky tu
    mv $file ${file:21:6}
done

# for file in *[2].TXT; do
#     mkdir  "2-"$file
#     mv $file "2-"$file
# done

#ABC_News_Transcripts_1988_1
