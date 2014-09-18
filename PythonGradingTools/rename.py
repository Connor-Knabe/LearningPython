import os
lab = ""
for filename in os.listdir("."):
	if filename.startswith("Lab "):
		lab = filename.split(" ")
		os.rename(filename, filename[6:12])
print lab