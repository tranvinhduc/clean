#!/usr/bin/zsh

for file in $1/**/*.txt ; do
    cp -n  $file  $2
done


