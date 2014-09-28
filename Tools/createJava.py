import sys
import os
#print sys.argv[1]

for line in sys.stdin:
    print line

print sys.argv[1]
file = open(sys.argv[1] + ".java", 'w+')

if (file):
    file.write("Testa\t\t\n\naa\taa\n")
