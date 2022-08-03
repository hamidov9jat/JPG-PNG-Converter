# Get command line arguments
# Check the folders
import pathlib
from sys import argv
from pathlib import Path

#get cmd arguments

n = len(argv)

if n == 3:
    # check for the folder name
    source_folder = pathlib.Path(argv[1])
    destination_folder = pathlib.Path(argv[2])




