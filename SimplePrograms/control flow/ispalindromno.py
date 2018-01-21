def IsPalindrom(no):
	rem=0
	sum=0
	tempNo=no
	while tempNo>0:
		rem=tempNo%10
		sum=(sum*10)+rem
		tempNo=int(tempNo/10)
		#print("no is:",rem)
	if no==sum:
		return True
	return False
def main():
	no1=eval(input("enter No:"))
	result = IsPalindrom (no1)
	if result :
		print("No is palindrom")
	else:
		print ("no is not palindrom")
if __name__=="__main__":
	main()