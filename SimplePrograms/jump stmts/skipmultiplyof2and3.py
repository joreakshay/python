def SkipMultipleof2and3(iStart,iEnd):
   for x in range(iStart,iEnd):
      if x %2==0 or x%3==0 :
         continue
      print(" ",x)
def main():
   iStart=eval(input("Enter start:"))
   iEnd=eval(input("Enter end:"))
   SkipMultipleof2and3(iStart,iEnd)
if __name__ == "__main__":
   main()