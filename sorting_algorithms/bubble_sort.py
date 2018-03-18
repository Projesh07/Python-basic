def bubble(lst):

	Swap=True
	temp=0

	while(Swap):
		Swap=False

		print 'after a cycle  list value {}',format(lst)
		print '-------------------------'
		print '-------------------------'
		print '-------------------------'
		for i in range(len(lst)-1):
			print 'before swaping lst value {}',format(lst)
			if lst[i]>lst[i+1]:
				lst[i],lst[i+1]=lst[i+1],lst[i]
				Swap=True
				print 'after swaping lst value {}',format(lst)

	return lst

lst=[5,3,45,6,7,9,0,-1]

result=bubble(lst)

print result 					
