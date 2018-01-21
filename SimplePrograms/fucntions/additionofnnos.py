def Addition(*args):
   sum=0
   for x in args:
      sum=sum+x
   return sum
def main():
   print("sum of n nos=",Addition(1,2,3,4,5,6,7,8,9))

if __name__ == "__main__":
   main()