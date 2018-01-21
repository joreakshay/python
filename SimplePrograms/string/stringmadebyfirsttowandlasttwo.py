def MadeString(string1):
	return string1[:2]+string1[-2:]
def main():
	string1=input("Enter String:")
	string2=MadeString(string1)
	print("string is:",string2)
if __name__=="__main__":
	main()
