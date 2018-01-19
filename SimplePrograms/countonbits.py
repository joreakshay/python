from sys import getsizeof
def CountOnBits(num):
	x=1
	count=0
	while(abs(num)>=x):
		if num<0:
			if (num & x ==0):
				count+=1
		else:			
			if (num & x !=0):
				count+=1
		x=x<<1
	if num<0:
		count=((getsizeof(num)*8)-count)
	
	return count
			
def main():
	num=input("Enter no:")	
	print("No of on bits are :{}".format(CountOnBits(num)))
	
if __name__=="__main__":
	main()
