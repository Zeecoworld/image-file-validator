This is a simple pluggable python library that validate image file and size useful for all 
type of python applications.


####How to use the packages


from image_file_validator.image_file_validator import check_file_type

check_for_image_size = check_file_type("./hello.png")

#FOR USAGE 
if check_for_image_size == True:
   print("valid image file")
else:
    print("invalid image file)



# PIP PACKAGE DEPENDECIES

pip install filetype (pick your desired os)


### KINDLY MAKE PR for UPGRADE....



