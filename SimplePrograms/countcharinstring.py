def CountChars(string1,char1):
	cnt=0
	for ch in string1:
		if ch==char1:
			cnt+=1
	return cnt
def main():
	string1=input("Enter String:")
	char1=input("Enter char:")
	cnt=CountChars(string1,char1)
	print("Char count is:",cnt)
if __name__=="__main__":
	main()
