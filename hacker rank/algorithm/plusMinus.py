#!/bin/python

import sys

def plusMinus(arr):
    # Complete this function

    plus=0
    minus=0
    zeors=0



    for x in range(len(arr)):
    	if arr[x]>0:
    		plus=plus+1
    	elif arr[x]<0:
    		minus=minus+1
    	else:
    		zeors=zeors+1	
    	pass



    plus=plus/n
    minus=minus/n
    zeors=zeors/n

    print format(plus,".6f")
    print format(minus,".6f")
    print format(zeors,".6f")

if __name__ == "__main__":

	n=float(raw_input().strip())
	arr=map(int,raw_input().strip().split(' '))
	plusMinus(arr)