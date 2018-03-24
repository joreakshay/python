#Write a program to extract doc string from given python file.
import re
def finddocstrings(fd):
	line=fd.readline()
	isFun=False	
	while line!="":
		x=re.search("def",line)
		if x!=None :
			isFun=True
			line=fd.readline()
			continue
		line=fd1.readline()
	
def main ():
	fileName=input("Enter File Name to convert:")
	fd1=open(fileName)
	fd2=open(fileName[0:-3]+"_cnv"+fileName[-3:],"w")
	convertTo3x(fd1,fd2)
if __name__=="__main__":
	main()
