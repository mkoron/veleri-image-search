import fnmatch
import os

ROOT_DIR = raw_input("Enter directory: ")

def is_image_file(filename, extensions=('.jpg', '.png')):
	"""
	Return true if filename has appropriate extension.
	"""
	return any(filename.endswith(e) for e in extensions)

def image_files(folder):
	"""
	Return a list of image files.
	"""
	image_files = []
	[image_files.append(os.path.join(root, file)) for  root, _, files in os.walk(folder)
		for file in filter(is_image_file, files)]
	return image_files

print image_files(ROOT_DIR)