def getEid(employeeDetails):
	e_id=0
	for key in employeeDetails:
		if key >e_id :
			e_id=key
	return e_id+1
def Insert(employeeDetails):
	emp={}
	e_id=getEid(employeeDetails)
	emp["name"]=input("Enter Name :")
	emp["dob"]=input("Enter Date of birth:")
	emp["addr"]=input("Enter Address:")
	emp["salary"]=input("Enter Salary:")
	employeeDetails[e_id]=emp
def Create_Employee(employeeDetails):
	n=input("How many record :")
	for i in range(n) :
		Insert(employeeDetails)
def Modify(employeeDetails):
	emp={}
	e_id=input("Enter employee id to modify:")
	if e_id in employeeDetails :
		emp["name"]=input("Enter Name :")
		emp["dob"]=input("Enter Date of birth:")
		emp["addr"]=input("Enter Address:")
		emp["salary"]=input("Enter Salary:")
		employeeDetails[e_id]=emp
	else:
		print("Record not found")
def Search(employeeDetails):
	e_id=input("Enter employee id to search:")
	if e_id in employeeDetails :
		emp=employeeDetails[e_id]
		print("e_id\tName\tDob\tAddress\tSalary")	
		print("{}  {}  {}  {}  {}".format(e_id,emp["name"],emp["dob"],emp["addr"],emp["salary"]))
	else:
		print("Record not found")
def Delete(employeeDetails):
	e_id=input("Enter employee id to Delete:")
	if e_id in employeeDetails :
		del employeeDetails[e_id]
		print("Record remove successfully")			
	else:
		print("Record not found")
def Display(employeeDetails):

	print("e_id\tName\tDob\tAddress\tSalary")
	for e_id in employeeDetails :
		Emp=employeeDetails[e_id]
		print("{}\t{}\t{}\t{}\t{}".format(e_id,Emp["name"],Emp["dob"],Emp["addr"],Emp["salary"]))

def Menu():
	print("1:Create Employee table\n2:Insert new employee recort\n3:Modify record\n4:Search employee\n5:Delete record\n6:Display\n7:Exit	")
	ch=input("Enter Choice:")
	return ch
def main():
	employeeDetails={}
	ch=Menu()
	while ch !=7:
		if ch==1 :
			Create_Employee(employeeDetails)
		elif ch==2:
			Insert(employeeDetails)
		elif ch==3:
			Modify(employeeDetails)
		elif ch==4:
			Search(employeeDetails)
		elif ch==5:
			Delete(employeeDetails)
		elif ch==6:
			Display(employeeDetails)	
		ch=Menu()
if __name__=="__main__":
	main()