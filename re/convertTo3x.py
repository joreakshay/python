#Write a program to accept python 2.x script & convert it to be compatible with 3.x.
import re
def convertTo3x(fd1,fd2):
	line=fd1.readline()	
	while line!="":
		x=re.search("print",line)
		if x!=None :
			line=line[0:x.end()+1]+"("+line[x.end()+1:-1]+")\n"
		fd2.write(line)
		line=fd1.readline()
	
def main ():
	fileName=input("Enter File Name to convert:")
	fd1=open(fileName)
	fd2=open(fileName[0:-3]+"_cnv"+fileName[-3:],"w")
	convertTo3x(fd1,fd2)
if __name__=="__main__":
	main()
