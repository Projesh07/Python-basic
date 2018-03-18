def selection(lst):


	for i in range (len(lst)): #Go to until sorted arry

		min_val=i
		for j in range(i+1,len(lst)): #Go to till unsorted

			if lst[j]<lst[min_val]:
				min_val=j
				# print min_val
		lst[i],lst[min_val]=lst[min_val],lst[i]

	return lst





lst=[5,3,45,6,7,9,0,-1]

result=selection(lst)
print result