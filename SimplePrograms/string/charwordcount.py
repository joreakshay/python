def WordCount(string1):
   wcount=0
   ccount=0
   flag =False
   for x in string1:
      if x==" " and flag ==False:
         wcount+=1
         flag=True
      elif x!=" ":
         flag=False
      ccount+=1
   print("word count is %d and char count is %d",wcount,ccount)
   
def main():
   string1=input("Enter string:")
   WordCount(string1)
if __name__=="__main__":
   main()
