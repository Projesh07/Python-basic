


#We need to consider four things in stack
#One - stack list (which will start from empty)
#Two -push in stack(Wich will start from begaining and point to the index of pussing an element new element 
#Always push in top of last element)
#Three pop from stack (we need to pop from top it is like last element inserted need to pop first)
#And at last we need to check is the stack is empty or not so that all the element we push are poped or not
#From the stack
#Basic reminder Last in first out (Or First in last out)-> Remeber life of sex (stack-life)

#So according to the algorithm 1st we need an empty array/list

def create_stack():
	stack=[]

	return stack
#Second we need to push element to the stack

#To push something in a list in python we can use append
#So wehre we need to push? in stack right. 
#And what  we need to push? an element. 
#So push_stack() function will take? yes you are right two arguments stack[] list and elemnt to push in the stack

def push_stack(stack,item):

	stack.append(item)

#Third we need to pop element so from the existing stack
#Like push it is just reverse way 
#So from where we need to pop? from the stack Right?
#and what we need to pop? an element but in this case remeber we don't need to pop a specific 
#Element because we always pop from the top of the stack and we are removing the memory/or index with that 
#So remeber pop don't need an element as an argument like push
#By default, pop without any arguments removes the last item:

#So pop_stack() function only need one argument and which is the stack[] list? clear?

def pop_stack(stack):

	if isEmpty(stack):
		print 'Stack is emapty'
	else:	
		return stack.pop()

#Lastly we need to check our stak is empty or not. if empty we can't pop from our stack
#But we can push into the stack

#So we need to check our stak is empty or not
#If empty return the lenght of our stack[] list
#So as like pop we need only one argument and this is our stack[] list for this isEmpty() functions

def isEmpty(stack):
	return len(stack)==0




#Now insturct your brain what to to with those functions?
#1st we need to call create stack which will initalise a stack list
#second we need to call push_stack to insert/push an element into our stack list(remebered it takes two args.)
#Do it for several times and print the stack  you will see what you pushed last it is in the begaining ?
#and that is what is stack algorithm statisfied. so far so good now

#Now to remeove an element we need to call pop_stack() function
#Remebered that pop remeove element from top and pop_stack() function takes one arguments
#So if we want to remove 15 and 13 how many times we need to call pop_stack() 

#If Number pop  of time you  is greater than you push you will see an message stack is empty?

#Because we are poping if stak is not empty

def main():
	stack=create_stack()    
	push_stack(stack,10)	# 15
	push_stack(stack,12)	# 13
	push_stack(stack,13)	# 12
	push_stack(stack,15)	# 10
	print stack

	pop_stack(stack)
	pop_stack(stack)
	pop_stack(stack)
	pop_stack(stack)
	pop_stack(stack)
	print stack



main()

#I think Stack data structure concept is clear now.

#Remeber one thing whenever we push element in our stack the stackpointer move to the next










