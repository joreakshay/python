
import subprocess
import time
def processInfo():
	cnt=1
	while cnt!=10:
		x=subprocess.check_output(["ps","-A"])
		print(x)
		time.sleep(1000)
		cnt+=1
def main():
	processInfo()
if __name__=="main":
	main()
