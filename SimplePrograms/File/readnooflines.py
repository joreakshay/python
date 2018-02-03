def readlines(fd,no):
	lines=[]
	line=(fd.readline())
	while line!="" and no>0:
		lines.append(line)
		line=fd.readline()
		no-=1
	return lines
def main():
	fileName=input("Enter file name :")
	no=input("Enter no of lines:")
	fd=open(fileName)
	lines=readlines(fd,no)
	print(lines)
if __name__== "__main__" :
   main()