#List work with siquential data
list_data=['Python','Java','Php','Perl']
print (list_data)
#Output ['Python','Java','Php','Perl']
#lenght is get by len() function

print (len(list_data))   
#Output is 4 (length of list_data)

#Inserting data in last position
#By append() its take arguments which are need to be insert at last position
list_data.append('Javascript')
print (list_data)  

#Output ['Python', 'Java', 'Php', 'Perl', 'Javascript']

#removing data from last position
#By pop() its take arguments which are need to be remove from last position


list_data.pop()
print (list_data)  

#Output ['Python',Java', 'Php', 'Perl']

#If you specify index number than it will remove that indexd element from list
var_popd=list_data.pop(2)

print (list_data) 
#Output ['Python','Java', 'Perl'] 
#Pop return a value so what value actuly poped we can store
print (var_popd) 
#Output Php


#If index is excide the length value
#list_data.pop(4)
#print (list_data)  

#Output Pop index out of range

#list_data.pop('Javascript')
#print (list_data)  

#Output an integer is required



#We can get list valeu by index  by square bracket
#List index start from 0 and goes to len()-1
print (list_data[0]) 
#Output Python

#We can use List index start from end with negatiove 
#It start from -1 and goes to -len()

print (list_data[-1]) 
#Output Perl
print (list_data[-len(list_data)]) 
#Output Python

#To get list values from one index to another we use [:]
print (list_data[0:2]) 
# Output ['Python', 'Java'] where 0 is start index and 1 is last index
#So start index is included but last index is not 

#if we dnt specify the start index it will get from 0 index
print (list_data[:2]) 
#Output ['Python', 'Java'] 

#if we dnt specify the last index it will get from specified start index to  last index
print (list_data[2:]) 
#Output ['Perl'] 

#For inserting into a specific list and begning 
#We use insert() function which tage two args
#1st one index where we want to insert 2nd the inserting value.
list_data.insert(0,'C language')
print (list_data)
#Output ['C language', 'Python', 'Java', 'Perl']

list_data.insert(2,'C++ language')
print (list_data)
#Output ['C language', 'Python', 'C++ language', 'Java', 'Perl']

#To extend a list we use extend()  function
#It takes only one arg
#if we insert a list in another list it will insert the whole list 
#Into a index of the list as example

list_data2=['I love','Python']
list_data.insert(0,list_data2)
print (list_data)
#Output [['I love', 'Python'], 'C language', 'Python', 'C++ language', 'Java', 'Perl']

#To extend a list we use extend()  function
#It takes only one arg ( list_data.extend(0,list_data2) extend() takes exactly one argument (2 given)

list_data2=['I love','Python']
list_data.extend(list_data2)
print (list_data)

#Output [['I love', 'Python'], 'C language', 'Python', 'C++ language', 'Java', 'Perl', 'I love', 'Python']


#To remove specific value we use remove()
#It takes only one argument what we want to remove
#list_data.remove(0,list_data2) remove() takes exactly one argument (2 given)

list_data.remove(list_data2)
print (list_data)
# Output ['C language', 'Python', 'C++ language', 'Java', 'Perl', 'I love', 'Python']

#For reversing a list we use reverse()
#It doen't take any argument

list_data.reverse()
print (list_data)
#Inorder it is ['C language', 'Python', 'C++ language', 'Java', 'Perl', 'I love', 'Python']
# Output['Python', 'I love', 'Perl', 'Java', 'C++ language', 'Python', 'C language']


#For Sorting a list we use sort()
#It  takes one arg which is optional
#By default it sorts accending order

list_data.sort()
print (list_data)
#Output ['C language', 'C++ language', 'I love', 'Java', 'Perl', 'Python', 'Python']
#For decending order we take reverse as an argument
list_data.sort(reverse=True)
print (list_data)
#Output ['Python', 'Python', 'Perl', 'Java', 'I love', 'C++ language', 'C language']

#But sort method return the actuall list as a sorted formate
#So we are replacing the actual list
#If we want to keep the actual list as it is and new one with sorted we need to use sorted() function
#It takes one arg
#var_sorted=sorted(list_data,reverse=True)
var_sorted=sorted(list_data)
print (var_sorted)
#Actual list ['Python', 'Python', 'Perl', 'Java', 'I love', 'C++ language', 'C language']
# sorted list ['C language', 'C++ language', 'I love', 'Java', 'Perl', 'Python', 'Python']

#There ar some list function for number list
# min(list_var) max(list_var) , sum(list_var) those return a value
print (max(list_data))
# Output Python

print (min(list_data))
# Output C language


#min max function can also be used with string list but sum is not

#To find a index number we use index()
#it takes only one argument which is value of the list

print (list_data.index('Python'))
#Output 0

#if the value is not present in the list it gives value error

#print (list_data.index('Math'))
#Output ValueError: 'Math' is not in list

#To check value in a list exist or not we use 'in'
#If it is present it returns true or False
print ('Math' in list_data)
#Output False

#we can iterate through a list using for in loop
for  data in list_data:
	print (data) 
#Output is following:

# Python
#Python
#Perl
#Java
#I love
#C++ language
#C language

#To access the index and value using for loop in list
#We use enumerate() it takes two args on is optional
#second arg can be start point as start=1

for  index,data in enumerate(list_data):
	print (index,data) 

#Output 
# (0, 'Python')
# (1, 'Python')
# (2, 'Perl')
# (3, 'Java')
# (4, 'I love')
# (5, 'C++ language')
# (6, 'C language')

for  index,data in enumerate(list_data,start=1):
	print (index,data) 
	
#Output 
# (1, 'Python')
# (2, 'Python')
# (3, 'Perl')
# (4, 'Java')
# (5, 'I love')
# (6, 'C++ language')
# (7, 'C language')

#To get all the list value as a string we use
# join() function
#It takes one argument list which we want to be string

str_list='    '.join(list_data)
print (str_list)

#Output PythonPythonPerlJavaI loveC++ languageC language
#We are joining a list with a string 

str_list='    '.join(list_data)
print (str_list)
#Output Python    Python    Perl    Java    I love    C++ language    C language

#String can be form into a list by split() function
#It takes one arg where we want to split 

str_to_list=str_list.split('    ')
print (str_to_list)

#Output ['Python', 'Python', 'Perl', 'Java', 'I love', 'C++ language', 'C language']

