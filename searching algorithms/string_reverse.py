
#First we need to implement the stack algorithm
#According to stack algo. we know four things to do.
#First create a emapty stack 
#Second push element into stack
#Third pop element from stack
#Fourth we can pop until stack is empty
#As stack followes last in first out and bottom to top for pushing and top to bottom for poping
#So we need to do step by step

#1st creating stack 

def create_stack():
	stack=[] #initalize our stack list

	return stack 


#2nd push into stack 

def push_stack(stack,item):
	stack.append(item)



#3rd pop from the stack if stack is not empty
def pop_stack(stack):
	if is_Empty(stack):
		print 'stack is empty'
	else:
		return stack.pop()	
	
#Fourth check if the stack is empty or not 

def is_Empty(stack):
	return len(stack)==0


#Finally the main function for whichand where is main goal of our stack implemnetation start

#So for reversing a string using stack we need to create the stack first
#Then each of the string char need to push into the stack 
#Then those string need to be poped from the stack 
#As pusing a string its form a list from start to end sequintially as the given string is (bottom up approch)
#And pop is just removing the elementfrom the top of the stack so, after poping we will get the reverse of the string 


def main():

	#lets given string
	given_string='stack exchange'

	#create the stack
	stack=create_stack()

	for item in range(len(given_string)):
		# print given_string[item]
		push_stack(stack,given_string[item])

	#lets take a empty string variable where can we store our reverse string
	reverse_string=''

	#Now from stack we need to pop our pushed string elements and store into poped variable 
	#Because pop() function return a value which element is poped 

	for item_pushed in range(len(stack)):
		poped=stack.pop()
		reverse_string+=poped
			


	#Finaly print the reversed string (How easy it is . isn't it?)	

	print reverse_string
main()		




