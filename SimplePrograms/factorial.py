#non recursion
def Factorial(num):
   fact=1
   for x in range(1,num+1):
      fact=fact*x
   return fact
#direct recursion
def FactorialR(num):
   if no<2:
      return 1
   return(num*(FactorialR(num-1)))

def main():
   print("Factorial of 5 is =",FactorialR(5))
if __name__=="__main__":
   main()
