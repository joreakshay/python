def Pattern(row):
	
	for i in range(row):
		for j in range(row-i):
			print "*",
		for j in range(i):
			print " ",
		for j in range(i-1):
			print " ",
		n=i
		if n==0:
			n=1
		for j in range(row-n):
			print "*",		
		print
def main():
	Pattern(4)
	
if __name__=='__main__':
	main()

