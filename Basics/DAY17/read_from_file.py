#To read all contents in the file
f = open("file_basics.txt","r")
content = f.read()
print(content)
f.close()
#To read lines into list
f = open("file_basics.txt")
lines = f.readlines()
print(lines)
f.close()
#To read single line
f = open("file_basics.txt")
line = f.readline()
print(line)
f.close()