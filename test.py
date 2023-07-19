from image_file_validator.image_file_validator import check_file_type



#TESTING THE PYTHON PACKAGE

checking_for_mime = check_file_type("./hh.png")


#FOR USAGE 
# if check_for_image_size == True:
#    print("valid image file")
# else:
#     print("invalid image file)


print(checking_for_mime)