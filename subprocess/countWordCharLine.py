
import subprocess	
def main():
	fd=open("a.txt")
	x=subprocess.Popen(['wc'],stdin=fd)
if __name__=="__main__":
	main()
