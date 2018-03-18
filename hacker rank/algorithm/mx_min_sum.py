import sys

def miniMaxSum(arr):
    # Complete this function
    max_sum=0
    min_sum=0
    fst=True
    for i in range(len(arr)):
    	_sum=0
    	for j in range(len(arr)):
    		if j!=i:
    			print ("no")
    			_sum+=arr[j]

    			
    				
    	print("_sum {}".format(_sum))		
    	if _sum>max_sum:
    		max_sum=_sum
    	if fst:
    		fst=False
    		min_sum=_sum

    	if _sum<min_sum:
    		min_sum=_sum

    print("{} {}".format(min_sum,max_sum))
			



if __name__ == "__main__":
    arr = list(map(int, input().strip().split(' ')))
    miniMaxSum(arr)