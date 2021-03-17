#!/usr/bin/env python

# change color of Bologlyph icons and put the new files in a new directory
# 
#

import os, fnmatch

strokecolor = "#444444"
#strokecolor = "white"

outDir = "Bologlyph-"+strokecolor

print(outDir)

def findReplace(directory, find, replace, filePattern, outputDir):
    if not os.path.exists(outputDir):
        os.makedirs(outputDir)
        
    for path, dirs, files in os.walk(os.path.abspath(directory)):
        for filename in fnmatch.filter(files, filePattern):
            filepath = os.path.join(path, filename)
            filepathO = os.path.join(outputDir, filename)
            #print(filename);
            with open(filepath) as f:
                s = f.read()
            s = s.replace(find, replace)
            with open(filepathO, "w") as f:
                f.write(s)

findReplace("Bologlyp-black8",'stroke="black"','stroke="'+strokecolor+'"',"*.svg",outDir)
#
# in the same manner, it is possible to change the stroke size by replacing
# 'stroke-width="8"'  with 'stroke-width="'+X+'"' where X is the new stroke widht
#
