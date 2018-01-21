def countvowelandconsonant(string1):
	vcount=0
	ccount=0
	for ch in string1:
		if ch in "aeiou" or ch in "aeiou":
			vcount+=1
		else:
			ccount+=1
	print("vowels=",vcount)
	print("Consonant=",ccount)
def main():
	string1=input("Enter string :")
	countvowelandconsonant(string1)
if __name__=="__main__":
	main()