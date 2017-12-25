def sumofoddrange(iStart,iEnd):
	sum=0
	for x in range(iStart,iEnd):
		if x&1==1:
			sum=sum+x
	return sum
def main():
	iStart=eval(input("Enter start:"))
	iEnd=eval(input("Enter end:"))
	if iStart<iEnd:
		print("Sum of odd range=",sumofoddrange(iStart,iEnd))
if __name__=="__main__":
	main()