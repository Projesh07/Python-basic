
list=[5,6,7,8,9]


# for item in range(len(list)-1,-1,-1):


# 			temp=list[item]

# 			list[item]=list[0]
# 			list[0]=temp

# print list			


for item in range(0,len(list),1):
	print item

	for item2 in range(item,len(list),1):


			temp=list[item]

			list[item]=list[item2]
			list[item2]=temp

print list			



						


# list=[1,2,3,4,5]
# # temp=[None]*len(list)

# for item in range(len(list)-1,-1,-1):
# 		print item
		
		
# 		# temp[item]=list[item]


# print temp		

