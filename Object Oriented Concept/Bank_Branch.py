from bank_account import Bank_Account

class Bank_Branch:
	
	def __init__(self,amt=0):
		self.accounts={}
	def __del__(self):
		del(self.accounts)
	def create(self):
		obj=Bank_Account()
		self.accounts[obj.accountNo]=obj
	def deposit(self,accountNo,amt):
		self.accounts[accountNo].deposit(amt)
	def withdraw(self,accountNo,amt):		
		self.accounts[accountNo].withdraw(amt)
	def showBal(self,accountNo):
		print("account bal={}".format(self.accounts[accountNo].amt))
	def trancefer(self,accountNo1,accountNo2,amt):
		self.accounts[accountNo1].withdraw(amt)
		self.accounts[accountNo2].deposit(amt)
def menu():
	print(" 1 Deposit \n 2 Withdaw \n 3 Check bal\n 4 Trancefer\n 5 Back")
	ch = input("Enter choice :")
	return ch

def main():
	branch=Bank_Branch()
	print(" 1 Create Account \n 2 Already Account\n 3 Exit")
	ch1 = input("Enter choice :")
	while ch1!=3:
		if ch1==1:
			branch.create()
		elif ch1==2:
			ano=input("Enter acount no:")
			if ano in branch.accounts :
				ch = menu()
				while ch!=5:
					if ch==1:				
						amt=input("Enter amt:")
						branch.deposit(ano,amt)
					elif ch==2:				
						amt=input("Enter amt:")
						branch.deposit(ano,amt)
					elif ch==3:				
						branch.showBal(ano)
					elif ch==4:
						anoToTrancfer=input("Enter acount no:")
						amt=input("Enter amt:")
						branch.trancefer(ano,anoToTrancfer,amt)
					elif ch==5:
						break		
					ch = menu()
			else:
				print("Account not exits")
		print(" 1 Create Account \n 2 Already Account\n 3 Exit")
		ch1 = input("Enter choice :")	
if __name__=="__main__":
    main()