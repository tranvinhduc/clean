#!/usr/bin/zsh

for file in $1/**/*.$2 ; do
#    echo ${file:0:(-4)}.TXT
    mv -n  $file ${file:0:(-4)}.$3  
done
