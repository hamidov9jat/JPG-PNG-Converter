# Get command line arguments
# Check the folders
import pathlib
import sys
from sys import argv
import pathlib as pth
import os
import re

# source = pth.Path('./img_dst')
#
# jpegs = re.compile(r'^(.+)\.(jpg|jpeg)$')

# files = source.iterdir()
# for full_image_name in files:
#     # print(full_image_name)
#     image_name = jpegs.fullmatch(full_image_name.name)
#     # print(full_image_name.is_file())
#     # print(pth.PurePath(source).name)
#     if image_name is not None:
#         print(image_name.group(1))
    # print(full_image_name.name)


def image_names(img_format: str, directory='.'):
    match img_format.lower():
        case 'jpg' | 'jpeg':
            image_regex = re.compile(r'^(.+)\.(jpg|jpeg)$')
        case 'png':
            image_regex = re.compile(r'^(.+)\.png$')
        case _:
            print(f'{img_format=} is not supported!')
            sys.exit(1)
    source = pth.Path(directory)
    files = filter(pth.Path.is_file, source.iterdir())
    for full_image_name in files:
        image_name = image_regex.fullmatch(full_image_name.name)
        if image_name is not None:
            yield image_name.group(1)

print(list(image_names('jpg', './img_src')))