#Write a program to create an archive file of the specified folder using sh util module.
from shutil import make_archive

def main():
	fName = input("Enter file name: ")
	folderPath = input("Enter Folder path: ")
	make_archive(fName,'zip', folderPath)
	
if __name__=="__main__":
	main()