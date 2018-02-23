#Write a program to accept filename from user and display alternate 20 characters. Take alternate values from the user.
def DisplayAlternateCharacters(fd,no):	
	line=fd.read(no)
	while line!="":
		print(line)
		fd.seek(no,1)
		line=fd.read(no)		
	
def main():
	fileName=input("Enter file name :")
	no=input("Enter alternate no:")
	fd=open(fileName)
	DisplayAlternateCharacters(fd,no)
	
if __name__== "__main__" :
   main()