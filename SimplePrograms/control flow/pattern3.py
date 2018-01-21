def Pattern(n):
	string1="ABCD"
	for i in range(n):
		for j in range(i+1):
			print ("",string1[j],end='')
		print("")
def main():
	Pattern(4)
if __name__=="__main__":
	main()