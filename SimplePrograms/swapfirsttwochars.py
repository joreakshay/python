def SwapFirstTwoChar(string1,string2):
	tempstr1=string2[:2]+string1[2:]
	tempstr2=string1[:2]+string2[2:]
	print("1st string is:",tempstr1)
	print("2nd string is:",tempstr2)
def main():
	string1=input("Enter String:")
	char1=input("Enter char:")
	SwapFirstTwoChar(string1,char1)
if __name__=="__main__":
	main()
