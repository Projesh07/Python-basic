#Dictionaries are used as a KEy Value pairs (like associative array or hashmap)

var_dic= {'name':'python','used':'Yes'}

print (var_dic)

#Output {'used': 'Yes', 'name': 'python'}

#To get a specific value of a dic
#we use [] and put key in that sqr brackt

print(var_dic['name'])
#Output Python

#If key is not present than it gives key error

#print(var_dic["me"])

#Output KeyError: 'me'
#Key can be many type integer string and others

#We can put list inside a dic key as a value

var_dic= {'name':'python','used':['Yes','NO']}
print (var_dic)
#Output {'used': ['Yes', 'NO'], 'name': 'python'}

#We can access key of a dic using 
# get() method. it occurs no error if there is no key exist
# it takes two args. 1st  key ,2nd- default value if key doesn't exist

#print (var_dic.get())

#Output TypeError: get expected at least 1 arguments, got 0

print (var_dic.get('name'))
#Output python

#If key not exist and default value is not specified

print (var_dic.get('me'))
#Output None

#If key not exist and default value is  specified

print (var_dic.get('me','Not found'))
#Output Not found

print (var_dic.get('name','Not found'))
#Output Python
#So using get method is safe

#To new entry in a dictionary  we use ['key']

var_dic['me']='C++ Boss'

print(var_dic)
#Output {'me': 'C++ Boss', 'used': ['Yes', 'NO'], 'name': 'python'}

#To update the value of a key in a dictionary  we use ['key']

var_dic['name']='C++ Boss'

print(var_dic)
#Output {'me': 'C++ Boss', 'used': ['Yes', 'NO'], 'name': 'C++ Boss'}

#We can also update using update() method 
#It is usefull when we update multiple key values
#Update() mehtod takes dictionaries as an arguments
#argument dic are key value which are updated

var_dic.update({'name':'Python again','used':'NO'})

print(var_dic)

#Output {'me': 'C++ Boss', 'used': ['Yes', 'NO'], 'name': 'C++ Boss'}

#if argument dictionary contain any key  which are not present in the actual dic
#Dic will get extended with the new key
#So update() method modify the whole dic

var_dic.update({'name':'Python again','NEW':'Update'})

print(var_dic)

#Output {'me': 'C++ Boss', 'NEW': 'Update', 'used': 'NO', 'name': 'Python again'}

#If we don't pass any args to update() method than there will occur no error
#It will give the actual dic
var_dic.update()

print(var_dic)
#Output {'me': 'C++ Boss', 'NEW': 'Update', 'used': 'NO', 'name': 'Python again'}

#We can delete a key value of dic using del key word
#But it doesn't return any value

del var_dic['NEW']
print(var_dic)
#Output {'me': 'C++ Boss', 'used': 'NO', 'name': 'Python again'}

#We can also delte using pop method as like we do for list
#Pop method return a calue which is deleted 
#So we can store the removed value 
# TypeError: pop expected at least 1 arguments, got 0
#poped=var_dic.pop()

#poped=var_dic.pop('men')
#KeyError: 'men'
poped=var_dic.pop('me')

print var_dic 
print poped 
#Output {'used': 'NO', 'name': 'Python again'}
#Output C++ Boss

#We can find lenght of dic using len() function
#It will return number of keys in dic
print (len(var_dic))
#Output 2

#If we want to see all keys of dic
#We use keys() method
#TypeError: keys() takes no arguments (1 given)

#print (var_dic.keys('used'))
print (var_dic.keys())
#Output ['used', 'name']

#If we want to see all values of dic
#We use values() method
#TypeError: values() takes no arguments (1 given)
#print (var_dic.values('used'))

print (var_dic.values())
#Output ['NO', 'Python again']

#if we want to get both keys and values 
#We use items() method 
#TypeError: items() takes no arguments (1 given)
#print (var_dic.items('used'))
print (var_dic.items())
#Output [('used', 'NO'), ('name', 'Python again')]


#If we loop through a dic with only one value 
#It will return only the keys
for key in var_dic:
	print key

#Output used name

#If we loop through a dic with two value 
#It will return  the keys and values 
#For this we need to use items() method

for key,val in var_dic.items():
	print key ,val

#Output
#used NO
#name Python again

	
