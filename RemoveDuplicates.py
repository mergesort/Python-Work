lines_seen = set() # holds lines already seen
outfile = open("duplicatesremoved", "w")
for line in open("out.txt", "r"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()