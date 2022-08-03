# Get command line arguments
# Check the folders

from sys import argv
from pathlib import Path

#get cmd arguments

n = len(argv)

if n == 3:
    # check for the folder name
    source_folder = argv[1]
    destination_folder = argv[2]


