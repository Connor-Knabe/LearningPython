import os
for filename in os.listdir("."):
	if filename.startswith("Lab 1"):
		os.rename(filename, filename[6:12])