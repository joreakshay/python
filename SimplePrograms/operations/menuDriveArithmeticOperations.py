import sys
def add(no1,no2):
	return no1+no2
def sub(no1,no2):
	return no1-no2
def mult(no1,no2):
	return no1+no2
def div(no1,no2):
	if no2==0:
		return 0
	else:
		return no1/no2
def main():
	
	result =0.0
	while True:
		print("Press 1 to Add\nPress 2 to Sub\nPress 3 to Mult\nPress 4 to Div\nPress 5 to Exit")
		ch=eval(input("Enter choice:"))
		no1=eval(input("Enter No1:"))
		no2=eval(input("Enter No2:"))
		if ch ==1:
			result= add(no1,no2)
		elif ch==2:
			result=sub(no1-no2)
		elif ch==3:
			result=mult()
		elif ch ==4:
			result=div(no1,no2)
		elif ch ==5:
			sys.exit()
		print("Result=",result)
		
if __name__=="__main__":
	main()
