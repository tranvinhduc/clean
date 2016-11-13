#!/usr/bin/zsh
for i in *.txt
do
    mv -- "$i" "${i%.txt}"
done
