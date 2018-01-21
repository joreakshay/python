import math
def isprime(no):
	if(no%2)==0:
		return False
	for x in range(3,(int (math.sqrt(no))+1),2):
		if (no%x) ==0:
			return False
	return True
def PrintPrimeNoWithinRange(iStart,iEnd):
	if(iStart>iEnd):
		return False
	if (iStart%2)==0:
		iStart+=1
	for no in range(iStart,iEnd,2):
		if isprime(no):
			print(no)			
	return False
def main():
	iStart=input("enter Start:")
	iEnd=input("enter End:")
	PrintPrimeNoWithinRange(iStart,iEnd)
if __name__=="__main__":
	main()
