#Write a program to accept filename from user and display file in reverse order without using loop,readlines,without any built-in container. Hint: Use recursive program.
def DisplayReverse(fd):
	line=fd.readline()		
	if line=="":
		return 	
	DisplayReverse(fd)
	print(line)
		
def main():
	fileName=input("Enter file name :")	
	fd=open(fileName)
	DisplayReverse(fd)
	
if __name__== "__main__" :
   main()