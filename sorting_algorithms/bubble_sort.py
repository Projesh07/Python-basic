def bubble(lst):

	Swap=True
	temp=0

	while(Swap):
		Swap=False

		for i in range(len(lst)-1):
			if lst[i]>lst[i+1]:
				lst[i],lst[i+1]=lst[i+1],lst[i]
				Swap=True

	return lst

lst=[5,3,45,6,7,9,0,-1]

result=bubble(lst)

print result 					
