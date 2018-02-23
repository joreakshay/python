'''Write code to read a file of petrol prices in Maharashtra, Goa & Karnataka:
Jan 2015 81 67 84
Feb 2015 79 66 82
Mar 2015 78 65 81
Apr 2015 77 64 80
...
Output the average petrol price for each state to an output file named
petrol_avg_out.txt.
'''
def AveragePricesOfPetrol(fd):
	maharashtra=0
	goa=0
	karnataka=0
	count=0
	line=fd.readline()
	while line!="":
		split=line.split(" ")
		maharashtra+=int(split[2])
		goa+=int(split[3])
		karnataka+=int(split[4])
		count+=1
		line=fd.readline()
	
	fd.close()    
	fd=open("petrol_avg_out.txt","w")
	fd.write("maharashtra {}\n".format(maharashtra/count))
	fd.write("goa {}\n".format(goa/count))
	fd.write("karnataka {}\n".format(karnataka/count))
	fd.flush()
	fd.close()
def main():	
	fd=open(r"petrolprice.txt")
	AveragePricesOfPetrol(fd)
	
if __name__== "__main__" :
   main()