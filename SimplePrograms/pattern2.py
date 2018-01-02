def Pattern(n):
	for i in range(n):
		for j in range(n-i):
			print ("* ",end='')
		print("")
def main():
	Pattern(4)
if __name__=="__main__":
	main()