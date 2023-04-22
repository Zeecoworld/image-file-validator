This is a simple pluggable python library that validate image file and size useful for all 
type of python applications.


####How to use the packages

import os 
import magic 

imagecheck = ImageValidator("./hello.txt",2014)
check_for_image_mime = imagecheck.check_file_size("./hello.txt",2014)
check_for_image_size = imagecheck.check_file_mime_type("./hello.txt")


# PIP PACKAGE DEPENDECIES

pip install python-magic (pick your desired os)


### KINDLY MAKE PR for UPGRADE....



