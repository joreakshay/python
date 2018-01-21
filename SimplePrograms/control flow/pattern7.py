#!/usr/bin/python2.7
import math
def isprime(no):
	if(no%2)==0:
		return False
	for x in range(3,(int (math.sqrt(no))+1),2):
		if (no%x) ==0:
			return False
	return True
def getPrime(iStart):	
	while  isprime(iStart) ==False:		
		iStart+=1			
	return iStart
def Pattern(row):
	prime=2
	for i in range(row):
		for j in range(i+1):
			print prime,
			prime=getPrime(prime+1)
		print
def main():
	Pattern(4)
	
if __name__=='__main__':
	main()
