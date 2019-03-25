import os

directory = r"C:\Users\Ge-riz\Desktop\New folder\DICOM"

for root, dirs, files in os.walk(directory):
	for file in files:
		print(os.path.join(root, file))