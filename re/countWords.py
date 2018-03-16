import re
def CountWords(fd):
	ch=fd.read()
	bufferString=""	
	while ch!="":
		bufferString+=ch
		
		ch=fd.read()
	print(bufferString)
	print(re.findall("[\d+_+]\w*",bufferString,re.MULTILINE|re.IGNORECASE))
def main ():
	fileName=input("Enter File Name :")
	fd=open(fileName)
	CountWords(fd)
if __name__=="__main__":
	main()