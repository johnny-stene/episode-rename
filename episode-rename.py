#!/usr/bin/env python3

from os import system, listdir
from sys import argv, exit
from shlex import quote

try:
	directory = argv[1]
	namePrefix = argv[2]
	nameSuffix = argv[3]
	extension = argv[4]
except:
	print("Usage: episode-rename (directory) (prefix of name, before E**) (suffix of name, after E**) (extension)")
	exit(1)

for file in listdir(directory):
	if(file.endswith(nameSuffix) and file.startswith(namePrefix)):
		# Get episode number
		episodeNumber = file.split(namePrefix + "E")[1]
		episodeNumber = episodeNumber.split(nameSuffix)[0]
		print("Renaming episode number " + episodeNumber + " from " + file + " to Episode " + episodeNumber + extension)
		system("mv " + quote(file) + " Episode\ " + quote(episodeNumber) + quote(extension))
