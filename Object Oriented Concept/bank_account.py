
class Bank_Account:
	tempANo=1
	def __init__(self,amt=0):
		self.accountNo=Bank_Account.tempANo
		self.amt=amt
		Bank_Account.tempANo+=1		
	def deposit(self,amt):
		if amt>0:
			self.amt+=amt
	def withdraw(self,amt):
		if amt>0 and amt<=self.amt :
			self.amt-=amt
	def showBal(self):
		print("account bal={}".format(self.amt))

def menu():
	print(" 1 Deposit \n 2 Withdaw \n 3 Check bal\n 4 Exit")
	ch = input("Enter choice :")
	return ch

def main():
	accounts={}
	print(" 1 Create Account \n 2 Already Account\n 3 Exit")
	ch1 = input("Enter choice :")
	while ch1!=3:
		if ch1==1:
			obj=Bank_Account()
			accounts[obj.accountNo]=obj
		elif ch1==2:
			ano=input("Enter acount no:")
			curuntAccount=accounts[ano]
			ch = menu()
			while ch!=5:
				if ch==1:				
					amt=input("Enter amt:")
					curuntAccount.deposit(amt)
				elif ch==2:				
					amt=input("Enter amt:")
					curuntAccount.deposit(amt)
				elif ch==3:				
					curuntAccount.showBal()
				elif ch==4:
					break		
				ch = menu()
		print(" 1 Create Account \n 2 Already Account\n 3 Exit")
		ch1 = input("Enter choice :")	
if __name__=="__main__":
    main()