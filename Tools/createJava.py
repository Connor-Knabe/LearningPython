import sys
import os
#print sys.argv[1]

for line in sys.stdin:
    print line

fName = sys.argv[1]
file = open(fName + ".java", 'w+')

if (file):
    file.write("public class " + fName + " {\n    public static void main(String[] args) {\n        \n        \n    }\n}")
