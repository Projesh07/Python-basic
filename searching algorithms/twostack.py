# two stack from one array #GfG

#consider that we have one array and we need to store all the element of this array in two stack
#It doesn't matter we store array elemnet equally in two stack 
#We can store some into stack one and some into stack but none of the stack will be over flow and array all array elements are 
#Stored in stacks

#lets assume we have an array of n lenght

#And we have two stack to store the all elemnts so that none of the stack is overflowed


# first create a intial function for intializing all the variables we need
#We need a array / list variable
#We need stack one top pointer variable and stack two pointer vairable to point the index of the array

#Keep in mind stack one will go from left of the array and stack two will be from the right most of the array

#So stack_one_top=-1 (empty stack,because 0 is the start index for array)
# stack_two_top=length of the array because (right intex of the array is lenght-1)

# we are using class based python (oop python) where init will initalize all the required variable

class TwoStack():

	def __init__(self, number):
		self.list_size=number
		self.const_list=[None]*number #Where number is the length of list
		self.stack_one_top =-1		  #Initial pointer for stack one
		self.stack_two_top =number  #Initial pointer for stack two
		#rember when we push into satck one top pointer will increase by one 
		#When we push into stack 2 initail pointer will decrease by -1 (because we are started from last index of the array)

	#Now we will define two push function for two stack
	#but before push an element into stack we need to cheack is the stack is overflowed or not
	#We can check it by a logic that stack_one_top is less than stack_two_top+1 
	#Because if it is true than there is a middle index space in the array which can be pushed to a stack
	#Lets consider we have array of size 5
	#If we push two elemnt in stack_one and two element in stack_two theire top ponter will be at array index of
	# stack_one_top =1 stack_two_top =3 ( because it start from right of the array)
	# so stack_one_top < stack_two_top and there is left another index 2 between 1 and 3 where we can push a stack elemnt
	# but after pushing another time stack_one_top== stack_two_top and will be over flow error

	#so condition will be stack_two_top<stack_two_top-1 that means we have indexd elemnt in the array whick can be pushed
	def stack_one_push(self,item):
		if self.stack_one_top<self.stack_two_top-1:

			self.stack_one_top=self.stack_one_top+1
			self.const_list[self.stack_one_top]=item
		else:
			print 'stack one  is full'	
	def stack_two_push(self,item):
		if self.stack_one_top<self.stack_two_top-1:

			self.stack_two_top=self.stack_two_top-1
			self.const_list[self.stack_two_top]=item
		else:
			print 'stack two  is full'

	#Now for pop we need to check stack is under flow or not
	#If stack one top is >=0 we can pop from stack one beacuse it prove that stack is not empty

	#If stack two top is <number or size of array we can pop from stack two beacuse it prove that stack is not empty

	def stack_one_pop(self):
		if stack_one_top>=0:

			poped_val=self.const_list[stack_one_top]

			self.stack_one_top=self.stack_one_top-1

			return poped_val
		else:
			print 'stack one is under flowed'

	def stack_two_pop(self):
		if stack_two_top < self.list_size:

			poped_val=self.const_list[stack_two_top]

			self.stack_two_top=self.stack_two_top+1

			return poped_val
		else:
			print 'stack two is under flowed'	

#Now all done check it by check function
#No mattr how which order push into stack array will be same order which is stack_one + stack_two element

def check():
	number=5
	twostack=TwoStack(number)
	twostack.stack_one_push('stack_one')
	twostack.stack_two_push('stack_two')
	twostack.stack_one_push('stack_one')
	# twostack.stack_two_push('stack_two')
	twostack.stack_one_push('stack_one')
	twostack.stack_two_push('stack_two')

	#If you push another time there will be stack over flow error
	twostack.stack_one_push('stack_one')
	twostack.stack_two_push('stack_two')

	print twostack.const_list

check()						



		

