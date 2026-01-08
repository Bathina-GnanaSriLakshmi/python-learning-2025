# To overwrite existing content
f = open("file_basics.txt","w")
f.write("Hello Python \n")
f.write("I started file handling")
f.close()
f = open("file_basics.txt","a")
f.write("\nThis is one more line")
f.close()