from __future__ import print_function
import sys

def staircase(n):
    # Complete this function

    for i in range(n):
    	k=1+i
    	for j in range(n):
    		if j>=n-k:
    			print("#",end='')
    		else:
    			print(" ",end='')
    	print ('')	
	

    		

if __name__ == "__main__":
    n = int(raw_input().strip())
    staircase(n)