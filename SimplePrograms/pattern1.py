def Pattern(n):
	for i in range(n):
		for j in range(i+1):
			print ("* ",end='')
		print("")
def main():
	Pattern(4)
if __name__=="__main__":
	main()