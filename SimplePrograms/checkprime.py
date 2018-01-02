import math
def isprime(no):
   if(no%2)==0:
      return False
   for x in range(3,(int (math.sqrt(no))+1),2):
      if (no%x) ==0:
         return False
   return True
def main():
   no=eval(input("enter no:")
   if isprime(no):
      print("no is prime")
   else:
      print("no is not prime")
if __name__=="__main__":
   main()
