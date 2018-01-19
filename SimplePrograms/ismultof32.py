def IsMultOf32(num):
	return num&32==0
def main():
	num=input("Enter no:")
	if IsMultOf32(num):
		print("{} is mult of 32".format(num))
	else:
		print("{} is not mult of 32".format(num))
if __name__=="__main__":
	main()
