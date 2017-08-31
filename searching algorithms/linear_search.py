
#algorithm

#linear search start from left most index and compare each elements with searched elements till it is found
# if  element is found in the array than it return the index of the elemnts
#if not than it return -1 that means elements is not found

#Given list

# elements=[2,3,5,66,22,11,4,0,3]
# search_elments=0

# def linear_search():

# 	for i in range(len(elements)):
# 		if elements[i]==search_elments:
# 			return i
# 	return -1			

# check=linear_search()

# if check==-1:
# 	print 'elements not found'
# else:
# 	print 'elements present in {}th index'.format(check) 


elements=[2,3,5,11,17,22,25,33,37,39]

#mid 17 which is 
search_elments=eval(raw_input('enter a value'))
# search_elments=raw_input('enter a value')

# ValueError: invalid literal for int() with base 10: 'mm'
#ValueError: could not convert string to float 
#NameError: name 'toy' is not defined


def binary_search():
	first_index=0
	last_index=len(elements)-1
	loop_time=1
	while first_index<=last_index:


		mid_index=(first_index+last_index)/2

		if elements[mid_index]==search_elments:
			# print elements[mid_index]
			print 'loop runing {}th time'.format(loop_time)
			
			return mid_index
		elif elements[mid_index]<search_elments: 
			first_index=mid_index+1	
		else:
			last_index=mid_index-1
		loop_time=loop_time+1	
	return -1	


check=binary_search()
if check==-1:
	print 'elements not found'
else:
	print 'elements present in {}th index'.format(check) 







# By default the input function takes input as string format

# for other data type you have to cast the user input

# In Python 2 we use raw_input() function. it waits for the user to type some input and press return and we need to store the value in a variable by casting as our desire data type. Be careful when using type casting

# x = raw_input("Enter a number: ") #String input

# x = int(raw_input("Enter a number: ")) #integer input

# x = float(raw_input("Enter a float number: ")) #float input

# x = eval(raw_input("Enter a float number: ")) #eval input

# In Python 3 we use input() function which return a user input value

# x = input("Enter a number: ") #String input

# if you enter a string, int, float, eval it will take as string input

# x = int(input("Enter a number: ")) #integer input
# if you enter a string for int cast ValueError: invalid literal for int() with base 10:

# x = float(input("Enter a float number: ")) #float input
# if you enter a string for float cast ValueError: could not convert string to float

# x = eval(input("Enter a float number: ")) #eval input
# if you enter a string for eval cast NameError: name ' ' is not defined
# Those error also applicable for python 2





