''' WAP to accept a file name from user which contains data in following format
	audio=True
	HFt= False
	Gateway=True
	add data into dictionary (key=value)
'''
def GetConfigData(configString):
	
	key =""
	value=""
	if configString[0]!="#"	:
		splitstr=configString.split("=")
		if len(splitstr) >1 :
			key=splitstr[0]
			if "#" not in key :
				value=splitstr[1]
				splitstr=value.split("#")
				value=splitstr[0]
				splitstr=value.split("\n")
				value=splitstr[0]			
	return key,value
def readconfigdata(fd):
	fileData={}
	line=fd.readline()
	while line!="":
		if line[0]=="#" :
			line=fd.readline()
			continue
		key,value=GetConfigData(line)
		if key != "" and value != "" : 
			fileData[key]=value
		line=fd.readline()
	return fileData
def main():
	fileName=input("Enter file name :")
	fd=open(fileName)
	fileData=readconfigdata(fd)
	print(fileData)
if __name__== "__main__" :
   main()