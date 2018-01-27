
def Union(l1,l2):
	result= [x for x in l1 if x not in l2  ]
	result.extend(l2)
	return result
def main():
	l1=list(input ("Enter list 1:"))
	l2=list(input ("Enter list 2:"))	
	l3=Union(l1,l2)
	print l3
   
if __name__=="__main__":
	main()