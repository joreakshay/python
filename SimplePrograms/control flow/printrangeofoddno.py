def odd(lbound,ubound):
   if(lbound<ubound):
      for x in range(lbound,ubound):
         if (x&1) ==0:
            print(x)
def main():
   lbound,ubound=eval(input("lbound and ubound:"))
   
   odd(lbound,ubound)
if __name__=="__main__":
   main()
