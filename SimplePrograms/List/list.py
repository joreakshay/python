def addelement(l1,var):
   if type(var)==list :
   	   l1.extend(var)
   	else :
   	   l1.append(var)
def main():
   l1=[1,2,3]
   print l1
   addelement(l1,4)
   print l1
   l2=[5,6,7]
   addelement(l1,l2)
   print l1
   
if __name__=="__main__":
   main()