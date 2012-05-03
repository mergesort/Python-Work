#!/usr/bin/python

appendToFile = open("Corpus.txt", "r")
sortToFile = open("Sorted Corups.txt", "w")

for line in sorted(appendToFile, key = str.lower):
    sortToFile.write(line)