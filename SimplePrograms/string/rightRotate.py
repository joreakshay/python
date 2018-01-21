def RightRotate(string1,string2):
	if len(string1) != len(string2):
		return False
	return string1 in (string2+string2)
def main():
	string1=input("Enter string1 :")
	string2=input("Enter string2 :")
	if RightRotate(string1,string2):
		print("Strings are Right Rotate")
	else:
		print("Strings are not Right Rotate")
if __name__=="__main__":
	main()
	