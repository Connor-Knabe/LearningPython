import sys
import os
import subprocess

#to run python createJava.py fileNamehere

fName = sys.argv[1]
if(os.path.isfile(fName+".java")):
    cmd = "javac " + fName +".java" 
    subprocess.call("javac " + fName +".java", shell=True)
    cmd = "java " + fName +" "
    subprocess.call(cmd, shell=True)
else:
    file = open(fName + ".java", 'w+')
    file.write("public class " + fName + " {\n    public static void main(String[] args) {\n        \n        \n    }\n}")
    


