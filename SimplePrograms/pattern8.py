def Pattern(row):
	ch=65
	for i in range(row):
		for j in range(row-i):
			print " ",
		for j in range(i+1):
			print chr(ch+i-j),
		for j in range(i):
			print chr(ch+j+1),		
		print
def main():
	Pattern(4)
	
if __name__=='__main__':
	main()
