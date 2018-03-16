import re
def removeComment(fd):
	line=fd.readline()
	writeFD=open("removeCommentFile.txt","w")
	flag=False
	while line!="":
		x=re.search("'''",line)
		if x !=None :
			if flag :
				flag=False
				line=fd.readline()
				continue
			else :
				flag=True
		if flag :
			line=fd.readline()
			continue
		x=re.search("#",line)
		if x !=None :
			writeFD.write(line[0:x.start()]+"\n")
		else:
			writeFD.write(line)
		line=fd.readline()
	
def main ():
	fileName=input("Enter File Name :")
	fd=open(fileName)
	removeComment(fd)
if __name__=="__main__":
	main()