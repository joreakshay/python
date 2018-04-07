#!usr/bin/python
import time
def Logdecorator(func):
	print("Outer log Decorators")
	def log(args):	
		print("Log decorator")
		return func(str(time.time())+ " "+args)
	return log
def Namedecorator(func):
	print("Outer name Decorators")
	def name(args):	
		print("name decorator")
		return func("Akshay :"+ " "+args)
	return name
@Logdecorator
@Namedecorator
def logger(data):
	print("Logged {}".format(data))

def main():
	logger("hiii")
	time.sleep(1)
	logger("bye")
if __name__ =="__main__":
	main()
