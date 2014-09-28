import sys
import os
import subprocess


for line in sys.stdin:
    print line

fName = sys.argv[1]
if(os.path.isfile(fName+".java")):
    print "File Exists"
else:
    file = open(fName + ".java", 'w+')

if (file):
    file.write("public class " + fName + " {\n    public static void main(String[] args) {\n        \n        \n    }\n}")

cmd = "javac " + fName +".java" 

subprocess.Popen(cmd, shell=True)

cmd = "java " + fName

subprocess.Popen(cmd, shell=True)
