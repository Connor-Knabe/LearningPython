import os
for filename in os.listdir("."):
	if filename.startswith("Lab "):
		filename = filename.split("_")[1]
		print filename
		#os.rename(filename, filename[6:12])
