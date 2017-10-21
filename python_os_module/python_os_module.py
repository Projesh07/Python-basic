import os


#projesh Bhoumik
#Python and Django developer

#Here is smoe important functionality of python os module
#If anything wrong please feel free to modify and update
#It's in python 2 so if you are in python 3 run this with some changes

#dir ---> it gives the list of attributes and method of the os module

print dir(os)

# getcwd()  will give us current working directory (Your current os directory)
##print os.getcwd()

# chdir() change the current directory you specified
#it takes path as a string as a parameter

os.chdir('/media/drysalt/Development/python/python basics/')

print os.getcwd()

#give the list of file name in current dir
#It takes Exactly one argument path as a string 
#in this case '.' specify the current dir
print os.listdir('.')

# To create a directory we use mkdir()
#It takes atleast one argument (directory name as string)
#If the directory name already exist it will throw an file exist error
#We can only create only one base dir using this/ that means we can not create sub directories
#mkdir(name, mode)


os.mkdir('python-os')

#We can also create directory using makedirs() 
#It works same as mkdir() but difference is it can create sub directory
#if directories already exist it will give file exist error

os.makedirs('python-os/hello')

# rmdir() and removedirs() work as same removing directories
#But difference is rmdir just remove base directory if it is empty or don't have 
#files or sub directories
# removedirs() remove base directory and it's sub directory too
# both takes exactly one argument 'dir name' as string
# removedirs() have to remove sub-dirs first to remove the base dir otherwise will raise not empty error

#this will remove base and sub directory if not empty and exist

os.removedirs('python-os/hello')

#this will remove sub directoriy
os.rmdir('python-os/hello')

#to rename a file or directory we use rename()
#It takes exactly two arguments one--> file/dir name you want to change
#Two--->new file or dir name

os.rename('python-os','os-module')

#to get statastics or information about the file or directory
#we use stat()
#it tkaes exactly one argument the file or the dir name as string

print os.stat('os-module')

# posix.stat_result(st_mode=16893, st_ino=3677977, st_dev=2054, st_nlink=2, st_uid=1000, st_gid=1000, st_size=4096, st_atime=1508577819, st_mtime=1508577655, st_ctime=1508577819)
#it gives couple of information some are important like st_size

print os.stat('os-module').st_size

#for last modification 
#it gives timestamp result if you want to get it as human readbale date time just import datetime module
##print os.stat('os-module').st_mtime
#using date time module

from datetime import datetime

m_time=os.stat('os-module').st_mtime

#converting timestamp to date time
print datetime.fromtimestamp(m_time)

#to see the directory tree we use walk()
#It is basically a generator 
#IT yields with three tuple
#one--> Directory path two-->Directory names three->Directory having files
#it takes atleast one argument
#So get the values we need a forloop 

#it return 3 tuple
#see every time its going deep of the path/dir until the end

for dirpath,dirname,file_name in os.walk('.'):
	print 'path: {}'.format(dirpath)
	print 'dir name: {}'.format(dirname)
	print 'files: {}'.format(file_name)


#To get enviornment variable name use environ()
#environ will give you list of environment variable
#by get() we can get specific environment vairable it takes one args

print os.environ.get('HOME')

#os path module is used to work with path
#it has lots of methods 
#join() is usefull one which join two path with forward slash
#and it  takes two arg (two path)
path=os.path.join('.','hello2.txt')
print path

#if we want to create that file which is not exist we can use 
#folowwing with open() takes two args path_name and action-> read,write

with open(path,'w') as file:
	file.write('hello')

#base name return the file name
#it takes exactly one argument
print os.path.basename(path)

#dirname return the directory name
#it takes exactly one argument
print os.path.dirname(path)

#split return the both directory and file name
#it returns directory name 1st and file name second
#it takes exactly one argument
print os.path.split(path)

#path here used is not exist so if you want to check path exist or not use exists()
#if exist return true else false
#it takes exactly one argument

print os.path.exists(path)

#if you want to check the path is for file or dir you can use to method
# isdir()--> for checking directory or not
# isfile()--> for checking file or not
#it takes exactly one argument
#Both return true or false

print os.path.isfile(path)
print os.path.isdir(path)

# splitext() is used to get the path and extention
#it takes exactly one argument

print os.path.splitext(path)

print os.listdir('.')

#This will give you all usefull mehtods used in os.path module
print dir(os.path)



