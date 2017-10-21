#Hacker rank list problems

# N = int(raw_input())

# list_=[]

# for i in range(N):
# 	st=raw_input().split()
# 	cmd=st[0] #Return string if we used cmd=st[:0] it will be list so i had to care about it
# 	args=st[1:] #Return rest of the string as arg list

# 	if cmd=='print':
# 		print list_ ,
# 	else:

# 		# list_.insert()
# 		# print 'hello'+'me '.join(args) it only repeate recent string join that means me will repeated
	
# 		cmd+="("+ ",".join(args) +")"
# 		final_cmd='list_.'+cmd
# 		eval(final_cmd) #Python self exicutions


#Tuple converstion from list

# n = int(raw_input())
# integer_list = map(int, raw_input().split())
# print integer_list
# tp=tuple(integer_list)

# print hash(tp)
	

# for i in range(integer_list)





# mmeredith about a year ago

# Here is how I broke this down:

#     We need to read the first line of input to get it out of the way (it can be used to write a parser for the next line, but it isn't useful)

# n = raw_input()

#     Read in the second line -- this is just a single string ex. '1 2 3 4'

# input_line = raw_input()

#     Split the string by whitespace into a list

# input_list = input_line.split()

#     Note: This is a list of strings ex. ['1', '2', '3', '4'] But we want a list of integers ex. [1, 2, 3, 4]
#         We need to convert the list elements from strings to ints
#     [Simple] Option 1 (since we know the number of elements, n):

#     for i in xrange(n):
#         input_list[i] = int(input_list[i])

#     [Simple] Option 2 (if we are ignoring the first input line for some reason):

#     for i in xrange(len(input_list)):
#         input_list[i] = int(input_list[i])

#     [More Advanced] Option 3:

#     input_list = map(int, input_list)

#     [More Advanced] Option 4 (List composition):

#     input_list = [int(x) for x in input_list]

# Now input_list looks like this: [1, 2, 3, 4]

#     We need to convert our list of ints to a tuple of ints (as a list is not hashable, but a tuple is)

# t = tuple(input_list)

#     print the result

# print hash(t)

# Other Optimizations (Not necessary for credit here):

#     If the first input line == '0' then bail, there isn't anything interesting to parse
#     Call strip() on the input to remove trailing and leading whitespace.

# raw_input().strip()



    

#String swap lower upper

s='HackerRank.com presents "Pythonist 2".'


# s2='';

# for i in range(len(s)):
# 	print s[i],
# 	if s[i].islower()==True:
# 		s2+=s[i].upper()
# 	else:
# 		s2+=s[i].lower()
			
	 
        
# print s2, 

#or just use 
# print s.swapcase() 


# Split and join of string 

# def split_and_join(line):
#     l=line.split(" ")
#     s='-'.join(l)
    
#     return s


#String mutable process( string are not muteable but we need to do it forcefully)

# string="abracadabra"
# position=5
# character='k'
# # print string[:position]
# # print string[position+1:]

# st=string[:position]+character+string[position+1:]
# print st



#Sub string comparison


    # s1_len=len(string)
    # s2_len=len(sub_string)
    # counter=0
    # for i in range(s1_len):
    #     if string[i:i+s2_len]==sub_string:
    #         counter=counter+1
            
    # return counter

# s = raw_input()
# print s.isalnum() 

# s_all_num=[]
# for si in s:
# 	s_all_num.append(si)

# print (for s in s)
# print s[0:].isalpha()		

# 	# print s.isalnum() 
# 	print si.isalnum()

A=int(raw_input())
B=int(raw_input())
SOMA= A+B
print 'SOMA = {}'.format(SOMA)     

#           

# R=float(raw_input())
# print type(R)
# n=3.14159
# A=round(n*(R**R),4)
# print type(A)
# print 'A={}'.format(A)