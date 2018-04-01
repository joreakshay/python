
def fibonacciOfGivenRange(start,end):
	num1=1
	num2=1
	while num2<=end :
		if num1>=start and num1<=end:
			yield num1
		num2=num2+num1
		num1=num2-num1
def main():
	x=fibonacciOfGivenRange(5,50)
	for i in x:
		print i
if __name__=="__main__":
	main()
