#Tuples are as like as list but one major dif is
#Tuples are immuteble that means we can not change Tuples values
#List are muteable that means we can change the value

#Mutable

list_data_one=['Python','List','Tuples']
list_data_two=list_data_one

print(list_data_one)
print(list_data_two)

#Output 
#['Python', 'List', 'Tuples']
#['Python', 'List', 'Tuples']
list_data_one[0]='Other'

print(list_data_one)
print(list_data_two)

#Output omg how it changed to list_data_two values?
#Because bothe the list_data one and two are mutable and if we
#Change one of them it will get affected to others too
# ['Other', 'List', 'Tuples']
# ['Other', 'List', 'Tuples']

#Immutable
#Tuple are as like as list but we use paranthesis for tuples insted of brackets
#() - Tuples []-List

tuple_data_one=('Python','List','Tuples')
tuple_data_two=tuple_data_one

print(tuple_data_one)
print(tuple_data_two)

#Output 
#['Python', 'List', 'Tuples']
#['Python', 'List', 'Tuples']

#tuple_data_one[0]='Other'

print(tuple_data_one)
print(tuple_data_two)
#Output
#:( it TypeError
#'tuple' object does not support item assignment
#That because it's Immutbale

#As Tuples are immutble we can not use function like list to modify of tuples
#So it doesn't have much functions
#But we can access and loop through the tuples

#Other data type is Set 
#Set are as like as tuples or list but it is not sequential 
#But it can only contain value without duplicate
#We use curly braces in set

set_data= {'py','ja','ph','ph'}
print(set_data)

#set(['ph', 'py', 'ja'])#It doen't maintain order
#It removes duplicate two

#set intersection 
set_data= {'py','ja','ph','ph'}
set_data2= {'xy','ja','my','tyh'}
print(set_data.intersection(set_data2))
#Output set(['ja']) common in both sets

#set intersection 
set_data= {'py','ja','ph','ph'}
set_data2= {'xy','ja','my','tyh'}
print(set_data.difference(set_data2))
#Output set(['ph', 'py']) differnce of the two set

#set combine we use union 
set_data= {'py','ja','ph','ph'}
set_data2= {'xy','ja','my','tyh'}
print(set_data.union(set_data2))
#Output set(['xy', 'tyh', 'ph', 'py', 'my', 'ja'])
#Ignored duplicate 

#We can create a empty llist , Tuples and set by following

#List
emp_list=[]
#Or
emp_list=list()
#Tuplse
emp_Tuplse=()
#Or
emp_Tuplse=tuple()

#Set
emp_Tuplse={} #we can't create it bcz it is dictionary
#so
emp_Tuplse=set()




