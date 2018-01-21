
#direct recursion
def GCDR(a,b):
  
   if a==b:
      return a
   if a>b :
      return GCDR(a-b,b)
   else:
      return GCDR(a,b-a)
def LCM(a,b):
   return(a*b)/GCDR(a,b)
def main():
   num1=eval(input("enter 1st no="))
   num2=eval(input("enter 2nd no="))
   print("gcd of {} and {} is {}".format(5,10,GCDR(num1,num2)))
   print("gcd of {} and {} is {}".format(5,10,LCM(num1,num2)))
if __name__=="__main__":
   main()
