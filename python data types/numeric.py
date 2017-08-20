#Find the type of number (basically two type int and float)
#By type function which takes an argument of variable
num=3
print (type(num))
#Output <type int)

num=3.5
print (type(num))
#Output <type float)

#Arithmatic operators with number

#Addition        2+2
#Subtaction      2-2
#Multiplication  2*2
#Divisions       3/2
#Floor division  3//2
#Exponent        3**2
#Modulus         3%3

print (3+2)
#Output 5
print (3-2)
#Output 1
print (3*2)
#Output 6
print (3/2)
#Output 1.5 in python 3 1 in python 2
#Bcz in python 2 it takes floor value and int num
print (3 // 2)
#Output 1.5 it returns the floor value after divition

print (3**2)
#Output 9 it is squre of number

print (3%2)
#Output 1 it is reminder after division
print (3+2*2)
#Output 7
print ((3+2)*2)
#Output 10

#Incremanting 

num=1
num=num+1
print (num)
#Output 2
num +=1
print (num)
#Output 3

num *=2
print (num)
#Output 6

#Some built in function for number

#abs absulate value return without negative sign
# abs() takes one argument
num= -4.5

print (abs(num))
#Output 4.5
#Round to to nearest int value
#Round using round() method it takes 
#Two arg (2nd one is optional)
num =4.33
print (round(num))
#Output 4.0
#If 2nd arg is given than it rounded up to the nearest 
#with the postion after decimal point
num =4.33
print (round(num,1))
#Output 4.3

num =4.346
print (round(num,2))
#Output 4.35 see the difference

#Comparisons of numbers
#Comparions return boolean true or false

#Equal  3==2 #False
#Not equal 3 !=2 #True
#Greater than 3>2 #True
#Less than 3<2 #False
#Greater than or equal 3 >=2 #True
#Less than or equal  3<=2 #False
print (3<3)
#False
print (3>3)
#False
print (3>=3)
#True
print (3<=3)
#True
print (3!=3)
#False
print (3==3)
#True

#Difference of string concat and number addition

#Concatination

num1='123'
num2='227'
print (num1+num2)
#Output 123227

#Casting them to number and addition 
num1='123'
num2='227'
num1=int(num1)
num2=int (num2)
print (num1+num2)
#Output 350