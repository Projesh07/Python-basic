



#Open function take file name or file name with full path at postion one
#2nd arg is file mode read /write/append/read and write/
# 2nd args will r/w/a/r+
# 2nd args is optional if we don't give the mode default mode is read that means r
#When opening the file store it in a variable to work with
#The variable worked as an object
#if you open a file don't forget to close the file after working with it
#If you don't it may raise maximum file discriptor allowed by the system


file=open('read_test.txt')
file=open('work_test.txt','r')
file=open('work_test.txt','w')
file=open('work_test.txt','a')
file=open('work_test.txt','r+')

# file_object.name will give the file name which is opened

print file.name
#Output ->> work_test.txt

# file_object.mode will give the file mode which is opened
print file.mode

#Output ->> r

file.close()

#So for concerning opening and closing the file each time
#Python introduce a context manager
#we can do this by using with keyword
# the file is open but  action can be performed within/ outside the block of code using with:
#out side the block file object will be automatically destroy

with open('read_test.txt') as file_context:

	#File object is open within and this block close outside 
	#But we can access the object which is file_context inside/outside of the block
	#But action like read() and write() can not be done outside of the block
	#So we can acces the file_context object property like name,mode, but can nod do any action withe that object outside 

	contents=file_context.read()
	print contents
	
	#Read the content of the opened file and print it
	#but reading file like this with smale size is ok there is no memory stuff to think
	#But if it is large we don't want to get it load the giant file into memory
	#So we can use different methods 

	#This will return the file content as a list of lines
	#If we use both read and readlines list will be empty
	contents=file_context.readlines()
	print contents

	#This will return the file content of the first line
	#If we use both readline and readlines we will not get first line
	end=' '
	contents=file_context.readline()
	print contents		

	#So we can say that we can do only one type of action within the block
	#if use readline() again we will get the scond line of the file (Python 3)

	contents=file_context.readline()
	print contents,end

	#See there is a extra blank line each time because print statment endup with neeline by default
	#We can use end and emepty string pass through with it there will be no new line
	contents=file_context.readline()
	print contents,end

	#But this not good way to rread the whole file
	#So we can run a loop 
	for line in file_context:
		print line

	#We can controll the file content reading using read() with passing integer value as args
	#an integer is required
	#read() method read the file content by single char/elements
	#Dont forget to comment out above code which action is different
	contents=file_context.read(100)
	print contents,end

	#if we run read(100) agin wit will go for next 100 char till end of the file
	size_read=100
	contents=file_context.read(size_read)
	print contents,end


	#We can do this for large file using a loop instead doing again and again
	while len(contents)>0:
		print contents,end
		#we have to use read() again unless it will be an infinate loop
		contents=file_context.read(size_read)

	
	# tell() method returns the current position of the read
	print file_context.tell()	
	# seek() method point the current position of the read from where to read
	#It takes int as arg
	#Here reading is started from the first again
	file_context.seek(0)
	contents=file_context.read(size_read)
	print contents,end	



#--------------------This is about writinng into file -----------

#if we open a file as a read mode and want to write into it there will be an error so make sure the mode
#If file not exist write mode will first create the file and write into it and erase previous content
#If already exist than also write
#But in read mode it will throw an error file doen't exist

with open('write_test.txt','w') as file_context:
	file_context.write('hello')
	# if we use write again it will append to the file content
	#In that case we can set position for writing as we did for reading using seek() method
	#Remember seek() only overwrite the pointed position + length of the second content
	#Use file_context.write('M') to see the difference
	file_context.seek(0)
	file_context.write('hello')

#If file not exist append mode will first create the file and append into it to the end of the file
#If already exist than also write
#But in read mode it will throw an error file doen't exist

with open('append_test.txt','a') as file_context:
	file_context.write('hello')

#raeding and writing at a time ..
#It is usefull when coping one file content to another file
#We can do this by using nested with open()
with open('read_test.txt','r') as read_file_context:
	with open('read_test_copy.txt','w') as write_file_context:
		for read_line in read_file_context:
			write_file_context.write(read_line)

#To read and write with images
#We need to read the image as binary mode
#Then write  the image as copy in binary mode
#We can do this by using rb and wb (b specify that file reading and writing in binary mode)	
#For text it nothing will change it will work as normal read and write mode
#Incase of image there will be no image created if there no image exist it will throw an error

with open('cat.jpg','rb') as read_image_context:
	with open('cat_copy.jpg','wb') as write_image_context:
		for read_byte in read_image_context:
			write_image_context.write(read_byte)

#To prevent from reading and the writing whole file or image we can do by chunk or size	

with open('cat.jpg','rb') as read_image_context:
	with open('cat_copy2.jpg','wb') as write_image_context:
		chunk=500
		chunk_read= read_image_context.read(chunk)
		while len(chunk_read)>0:
			write_image_context.write(chunk_read)
			#For stoping infinate loop we must use chunk_read again
			chunk_read= read_image_context.read(chunk)


		


print file_context.name
#output ->>work_test.txt
print file_context.mode
#output ->> r
#print file_context.read() #ValueError: I/O operation on closed file



