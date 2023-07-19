from image_file_validator.image_file_validator import check_file_type



# imagecheck = ImageValidator("./hello.txt",2014)
# check_for_image_mime = imagecheck.check_file_size("./hello.txt",2014)
# check_for_image_size = imagecheck.check_file_mime_type("./hello.txt")

checking_for_mime = check_file_type("./hh.png")


print(checking_for_mime)