#file handling
#2 types of files:text file,binary file(not human-readable):images,audio,video
#4 file handling functions:open(),read(),write(),close()
#2 parameters in open()-file_name,mode
#4 type modes-'r':read,gives error if file does not exist
#'a':append, create new file if does not exist
#'w':write,create new file if does not exist
#'x':create a new file
#in addition,specify the file type
#'t'-text file,'b'-binary file


file=open('demofile2.txt','w')
file.write('hi,how are you' )
file.close()
file=open('demofile2.txt','r')
print(file.read())
#delete files
import os
os.remove("small.txt")


