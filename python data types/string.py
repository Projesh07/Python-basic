
#String with double qoutes
variable_string="Hello world"

print(variable_string)
#Output Hello world


#String with single qoutes you migh use escape char for this kind of string
variable_string='Python\'s world'

print(variable_string)
#Output Python's world

#String with multi line python use three double quotes
variable_string="""
Python\'s world
This is actuall fun and dream"""

print(variable_string)
#Output Python's world
#This is actuall fun and dream

#String function len(string var)
#It takes one arg and return length of the string
variable_string="ptyhon is my world"

print(len(variable_string))
#output 18


#GetCharacter using location in String 
#After varibale just use [] and specify number
variable_string="Hello world"


#Before : it is the starting point
#After : end point that exclude the end point
print(variable_string[0:6]) #Both same
print(variable_string[:6])
#Output Hello 
print(variable_string[6:11]) #Both same
print(variable_string[6:])
#Output World 
print(variable_string[6:10])
#Output worl 
#Bcz 1st index inclusive 2nd index is not cluded
#So string will be 6 to 9 w-6 o-7 r-8 l-9

print(variable_string[:])
#Output Hell World (or full string)

#Getting char using index
variable_string="Hello world"
print(variable_string[0])
#Output H
#print(variable_string[11])
#Output error index out range
#Becz indexing strat from 0 so 
#The last char will be at 10 in this case

#String lower() method. it doesn't take any args
#All char lower
variable_string="Hello world"
print(variable_string.lower())
#Output hello world

#String upper() method. it doesn't take any args
#All char upper
variable_string="Hello world"
print(variable_string.upper())
#Output HELLO WORLD

#String count() method. it  takes a string as args
#return number after counting
variable_string="Hello world"
print(variable_string.count('world'))
#Output 1
print(variable_string.count('l'))
#Output 3

#String find() method. it  takes a string as args
#return number where it's started from
variable_string="Hello world"
print(variable_string.find('world'))
#Output 6
print(variable_string.find('gone'))
#Output -1
#Bcz it return negative when it doen't find any matching string


#String replace()
#Takes two argument
#1st argument that you want to
#Second argument that u want to replace with
#Remebr it returns a new string after replacing
variable_string="Hello world"
new_var_string=variable_string.replace("Hello","Python")

print(new_var_string)
#Output Python world

#string concate using +sign
var_st1="Hello"
var_st2="World"
full_str=var_st1 + var_st2
print(full_str)

#Output HelloWorld (No space)

#string concate using +sign with space
var_st1="Hello"
var_st2="World"
full_str=var_st1 + ' ' +var_st2
print(full_str)

#Output Hello World (with space)

#string concate using placeholder with format() method
#format() takes all placeholder as arguments
var_st1="Hello"
var_st2="World"
full_str='{} {}'.format(var_st1,var_st2)
print(full_str)
#Output Hello world

#If format() arg is not eqaul to placeholder then it occur an error
#full_str='{} {}'.format(var_st2)
print(full_str)
#Output Error tuple index out of range

#another way to do this just placing string inside the place holder
#and placing f at the begening of the string
#It only possible at upper version of python 3
#full_str= f'{var_st1} {var_st2}'
print(full_str)
#Output Error tuple index out of range

#lastly 
# dir() method will show you all the method and attr
#Related to a variable in this case string variable

print(dir(variable_string))
#output all related method and attr

#You can do it by help function but 
#Help function works with class and methods
#so you have to pass help() function args as calss name or class method

# print (help(str))
# print (help(str.lower()))


# numList = ['1', '2', '3', '4']
# seperator = ', '
# print(seperator.join(numList))

# numTuple = ('1', '2', '3', '4')
# print(seperator.join(numTuple))

# s1 = 'abc'
# s2 = '123'

# """ Each character of s2 is concatenated to the front of s1""" 
# print('s1.join(s2):', s1.join(s2))

# """ Each character of s1 is concatenated to the front of s2""" 
# print('s2.join(s1):', s2.join(s1))


#str.islower()

#str.isupper()