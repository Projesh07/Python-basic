def combine(arr_one,arr_two):

	#two array combine into one.
	result=[]
	in_one,in_two=0,0
	if(arr_one !=None and arr_two !=None):
		arr_len=(len(arr_one)+len(arr_two))-1
		for i in range(arr_len):
			if in_one<len(arr_one) and in_two<len(arr_two):
				if arr_one[in_one]<arr_two[in_two]:
					result.append(arr_one[in_one])
					in_one+=1
				else:
					result.append(arr_two[in_two])
					in_two+=1

		result+=arr_one[in_one:]
		result+=arr_two[in_two:]
	else:
	    arr_len=0
	print('result')	
	print(result)
	print('-------')
	return result

	


def divide(in_arr):

	if int(len(in_arr))<=1:
		# print('done')
		return in_arr
	mid=int(len(in_arr)/2)
	# print(mid)
	
	left=divide(in_arr[:mid])	
	right=divide(in_arr[mid:])
	# print(left)
	# print(right)
	
	return combine(left,right)


in_arr=[5,3,2,7]
# print(in_arr[0:2])
result=divide(in_arr)
