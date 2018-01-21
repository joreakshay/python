def patern(n):
   for i in range(n):
      for j in range(n-i):
         print(" ",end="")
      for k in range(i*2+1):
         print("*",end="")
      print()
def main():
   patern(4)
if __name__=="__main__":
   main()
