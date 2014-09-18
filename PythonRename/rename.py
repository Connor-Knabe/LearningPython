import os
for filename in os.listdir("."):
	if filename.startswith("Lab "):
		os.rename(filename, filename[6:12])